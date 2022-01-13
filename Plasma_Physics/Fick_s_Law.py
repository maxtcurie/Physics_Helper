import numpy as np
import matplotlib.pyplot as plt

#this script plot the diffution 
#  with initial condition of:
#  n(x,t=0)=alpha*x+b
L=1.
t_max=30.
b=20000.
x=np.arange(-1.*L,L,0.01)
t=np.arange(0,t_max,1.)
#t=t[:5]
tau=np.arange(0.01,10.,0.001)
D=1. #Diffusion coeffient (J=D \nabala n)
alpha=1.

n_x_t=np.zeros((len(x),len(t)))

plt.clf()
plt.plot(x,[b]*len(x),color='red')
for i in range(len(t)):
    t_i=t[i]
    for tau_i in tau:
        #print(L/(2.*(D*tau_i)**0.5))
        B_i=2.*alpha*np.cos( L/(2.*(D*tau_i)**0.5) )\
            +4.*alpha/L*(D*tau_i)**0.5*np.sin( L/(2.*(D*tau_i)**0.5) )
        #print(B_i)
        n_x_t[:,i]=n_x_t[:,i]+B_i*np.sin(x/(D*tau_i)**0.5)*np.exp(-t_i/tau_i)
    n_x_t[:,i]=[b]*len(n_x_t[:,i])+n_x_t[:,i]
    plt.plot(x,n_x_t[:,i],color='blue',alpha=1.-t_i/np.max(t))
plt.xlabel('x')
plt.ylabel('density')
plt.ylim(0,np.max(n_x_t))
plt.show()
    

