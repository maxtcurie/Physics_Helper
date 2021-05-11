import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv


#cd .\Fluid\Linear_VS_nonlinar\Predator_Prey_Model
#python 0food_chain.py

num_mod=5
dt=0.001
tot_steps=1000
E_input=10
path='./'

#\frac{d x_i}{dt} = a_i x_i + \sum_{j} b_{ij} x_i x_j

gamma=np.zeros(num_mod)

gamma[0]=0.5    #fast growing
gamma[1]=0.51 
gamma[2]=0.505  #fast growing
gamma[3]=0.5051 
gamma[4]=0.495  #fast growing

k=np.zeros(num_mod)
k[0]=0.2
k[1]=0.3
k[2]=0.4
k[3]=0.5
k[4]=0.6

x=[1.]*num_mod

factor=1.
a=gamma*factor


def b_calc(k,gamma,E_input,x): 
    num_mod=len(x)
    b=np.zeros((num_mod,num_mod))
    E_tot=np.sum(x)
    for i in range(num_mod):
        for j in range(num_mod):
            if k[i]>k[j]:
                k_resonance=abs(k[i]%k[j])+0.01
            elif k[i]<=k[j]:
                k_resonance=abs(k[j]%k[i])+0.01

            k_distance=abs(k[i]-k[j])

            E_limit=E_input-E_tot

            if gamma[i]>gamma[j]:
                b[i,j]=  1.*gamma[i]*gamma[j]*( k_resonance * k_distance )**(-1.)
            else:
                b[i,j]= -1.*(gamma[i]*gamma[j])**(-1.)*( k_resonance * k_distance )**(-1.)
            if i==j: 
                b[i,j]= gamma[i]*gamma[j]*E_limit*0.1
    return b


def food_change_dt(a,b,x,t,dt):
    num_mod=len(x)
    dx=[0.]*num_mod

    for i in range(num_mod):
        for j in range(num_mod):
            #if i==j: pass
            #x_i(t+dt) = x_i(t) + ( a_i x_i + b_{ij} x_i x_j )dt
            dx[i]=dx[i]+(b[i,j]*x[i]*x[j])*dt
        dx[i]=dx[i]+a[i]*x[i]*dt
    for i in range(num_mod): 
        t=t+dt
        x[i]=x[i]+dx[i]

        with open(path+'Log/food_chain_'+str(i)+'.csv', 'a+', newline='') as csvfile:
            data = csv.writer(csvfile, delimiter=',')
            data.writerow([t,x[i]])
            csvfile.close()
    print('dx'+str(dx))
    print('x'+str(x))
    return t,x,dx

#******Start of the program******************

t=0.

for i in range(num_mod):
    with open(path+'Log/food_chain_'+str(i)+'.csv', 'w', newline='') as csvfile:
        data = csv.writer(csvfile, delimiter=',')
        data.writerow(['Time','x'])
        csvfile.close()


for it in range(tot_steps):
    b=b_calc(k,gamma,E_input,x)
    print('a:'+str(a))
    print('b:'+str(b))
    t,x,dx=food_change_dt(a,b,x,t,dt)
    if abs(np.average(dx))*10**7<abs(np.average(x)):
        print("sum of x: "+str(np.sum(x)))
        break

#Start to plot
plt.clf()
for i in range(num_mod):
    data=pd.read_csv(path+'Log/food_chain_'+str(i)+'.csv')
    plt.plot(data['Time'],data['x'],label='Animal'+str(i))

#plt.xlim(1.0,1.3)
#plt.ylim(1.0,1.3)
plt.legend()
plt.ylabel('number',fontsize=10)
plt.xlabel('time',fontsize=10)
plt.savefig(path+'Log/food_chain.png')
plt.show()
