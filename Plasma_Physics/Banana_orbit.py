import numpy as np
import matplotlib.pyplot as plt

def banana_plot(a):
    r0=1. 
    x=np.arange(-2,2,0.00001)
    
    (Width,Height)=(10,10)
    #r-r0=+-a*(1+x)**0.5
    #where r**2.=x**2.+y**2.
    plt.figure(figsize=(Width,Height),dpi=96)

    y1=((+a*(1.+x)**0.5+r0)**2.-x**2.)**0.5
    y2=((-a*(1.+x)**0.5+r0)**2.-x**2.)**0.5
    
    circle=(r0**2.-x**2.)**0.5

    plt.clf()
    plt.plot(x,y1,color='red',label='orbit')
    plt.plot(x,y2,color='red')
    plt.plot(x,-y1,color='red')
    plt.plot(x,-y2,color='red')
    plt.plot(x,circle,color='black',label='circle')
    plt.plot(x,-circle,color='black')
    plt.xlim(-3.,3.)
    plt.ylim(-3.,3.)
    plt.legend()
    plt.show()

banana_plot(a=0.01)
banana_plot(a=0.2)