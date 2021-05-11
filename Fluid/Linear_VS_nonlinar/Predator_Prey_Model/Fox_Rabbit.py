import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv


#cd .\Fluid\Linear_VS_nonlinar\Predator_Prey_Model
#python Fox_Rabbit.py

#Wiki of predator–prey equations: https://en.wikipedia.org/wiki/Lotka%E2%80%93Volterra_equations

#https://www.stolaf.edu/people/mckelvey/envision.dir/lotka-volt.html

#************start of user block**************

break_if_converge=1     #change to 1 if one want to stop the simulation if it converges
num_mod=2               #total number of animals
dt=0.1                 #size of time steps
tot_steps=2000           #total steps of time

#\frac{d x_i}{dt} = a_i x_i + \sum_{j} b_{ij} x_i x_j

x=[0.]*num_mod
a=[0.]*num_mod
b=np.zeros((num_mod,num_mod))

label_list=['fox', 'rabbit']

case_number= 0  #case0: Linear growth(exponential)
                #case1: Near steady state.
                #case2: Start from the random spot



# x[0]=number of Fox
# x[1]=number of Rabbit
x[0]=0.01
x[1]=100.

#natural growth rate for fox(0) and rabbit(1)
a[0]=-0.2    #growth rate for fox negative die if there is no food
a[1]= 0.04   #growth rate for rabbit

#interaction of fox and rabbit
b[0,0]=-0.0          #impact to fox    of interaction of fox    and fox    (internal competetion)
b[0,1]= 0.10          #impact to fox    of interaction of fox    and rabbit (fox eats rabbit and grow fater)
b[1,1]=-0.0          #impact to rabbit of interaction of rabbit and rabbit (internal competetion)
b[1,0]=-0.0005       #impact to rabbit of interaction of fox    and rabbit (rabbit eateb by fox and grow slower)

#b=np.zeros((num_mod,num_mod))

#************End of user block**************

path='./'

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
        x[i]=x[i]+dx[i]
        with open(path+'Log/food_chain_'+str(i)+'.csv', 'a+', newline='') as csvfile:
            data = csv.writer(csvfile, delimiter=',')
            data.writerow([t,x[i]])
            csvfile.close()
    t=t+dt
    print('dx'+str(dx))
    print('x'+str(x))
    return t,x,dx



if case_number==0: # case0: Linear growth(exponential)
    # x[0]=number of Fox
    # x[1]=number of Rabbit
    x[0]=0.1
    x[1]=0.6
    #stead state solution: {{Rabbit -> 0., Fox -> 0.}, {Rabbit -> 0.1, Fox -> 0.0666667}}


    #natural growth rate for fox(0) and rabbit(1)
    a[0]=-0.00   #growth rate for fox
    a[1]= 0.02   #growth rate for rabbit

    #interaction of fox and rabbit
    b[0,0]=-0.0         #impact to fox    of interaction of fox    and fox    (internal competetion)
    b[0,1]= 0.0          #impact to fox    of interaction of fox    and rabbit (fox eats rabbit and grow fater)
    b[1,1]=-0.0         #impact to rabbit of interaction of rabbit and rabbit (internal competetion)
    b[1,0]=-0.0           #impact to rabbit of interaction of fox    and rabbit (rabbit eateb by fox and grow slower)


elif case_number==1:  #case1: Near steady state.
    # x[0]=number of Fox
    # x[1]=number of Rabbit
    x[0]=0.06
    x[1]=0.09
    #stead state solution: {{Rabbit -> 0., Fox -> 0.}, {Rabbit -> 0.1, Fox -> 0.0666667}}


    #natural growth rate for fox(0) and rabbit(1)
    a[0]=-0.02   #growth rate for fox
    a[1]= 0.02   #growth rate for rabbit

    #interaction of fox and rabbit
    b[0,0]=-0.0         #impact to fox    of interaction of fox    and fox    (internal competetion)
    b[0,1]= 0.2          #impact to fox    of interaction of fox    and rabbit (fox eats rabbit and grow fater)
    b[1,1]=-0.0         #impact to rabbit of interaction of rabbit and rabbit (internal competetion)
    b[1,0]=-0.3           #impact to rabbit of interaction of fox    and rabbit (rabbit eateb by fox and grow slower)

elif case_number==2:   #case2: Start from the random spot
    # x[0]=number of Fox
    # x[1]=number of Rabbit
    x[0]=0.1
    x[1]=0.6
    #stead state solution: {{Rabbit -> 0., Fox -> 0.}, {Rabbit -> 0.1, Fox -> 0.0666667}}


    #natural growth rate for fox(0) and rabbit(1)
    a[0]=-0.02   #growth rate for fox
    a[1]= 0.02   #growth rate for rabbit

    #interaction of fox and rabbit
    b[0,0]=-0.0         #impact to fox    of interaction of fox    and fox    (internal competetion)
    b[0,1]= 0.2          #impact to fox    of interaction of fox    and rabbit (fox eats rabbit and grow fater)
    b[1,1]=-0.0         #impact to rabbit of interaction of rabbit and rabbit (internal competetion)
    b[1,0]=-0.3           #impact to rabbit of interaction of fox    and rabbit (rabbit eateb by fox and grow slower)



#******Start of the program******************

t=0.

print('a:'+str(a))
print('b:'+str(b))

for i in range(num_mod):
    with open(path+'Log/food_chain_'+str(i)+'.csv', 'w', newline='') as csvfile:
        data = csv.writer(csvfile, delimiter=',')
        data.writerow(['Time','x'])
        csvfile.close()


for it in range(tot_steps):
    t,x,dx=food_change_dt(a,b,x,t,dt)
    if abs(np.average(dx))*10**7<abs(np.average(x)):
        print("sum of x: "+str(np.sum(x)))
        if break_if_converge==1:
            break

#Start to plot
plt.clf()
for i in range(num_mod):
    data=pd.read_csv(path+'Log/food_chain_'+str(i)+'.csv')
    plt.plot(data['Time'],data['x'],label=label_list[i])

#plt.xlim(1.0,1.3)
#plt.ylim(1.0,1.3)
plt.legend()
plt.ylabel('number',fontsize=10)
plt.xlabel('time',fontsize=10)
plt.savefig(path+'Log/food_chain.png')
plt.show()

print('a:'+str(a))
print('b:'+str(b))

#solve for static 