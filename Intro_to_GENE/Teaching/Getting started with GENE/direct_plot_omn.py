#from get_nrg import *
#from get_rows import *
import numpy as np
import matplotlib.pyplot as plt

def get_rows():
    omn=np.empty(0,dtype='float')
    gamma1=np.empty(0,dtype='float')
    gamma2=np.empty(0,dtype='float')
    omn_th=np.empty(0,dtype='float')
    gamma1_th=np.empty(0,dtype='float')
    gamma2_th=np.empty(0,dtype='float')
    f=open('spec_comparison','r')
    read_in=f.read()
    read_in_lines=read_in.split('\n')

    trp=0.3333
    ky=0.2
#    omd=ky*np.sqrt(0.4/1.99)/1.0
    omd=ky
    ft=np.sqrt(2.*trp/(1.+trp))

    for j in range(len(read_in_lines)-1):
        nline=read_in_lines[j].split()
#        print j,nline
        omn=np.append(omn,float(nline[0]))
        gamma1=np.append(gamma1,float(nline[1]))
        gamma2=np.append(gamma2,float(nline[3]))
    for k in range(100):
        om=k/100.*40.
        omn_th=np.append(omn_th,om)
        tmp= np.imag(0.5*(om*ky+np.sqrt(complex((om*ky)**2-8.0*omd*40.0*ky))))
        tmp2= np.imag(0.5*(om*ky+np.sqrt(complex((om*ky)**2-8.0*omd*40.0*ky*(1.+ft)/(1.-ft)))))
        gamma1_th=np.append(gamma1_th,tmp)
        gamma2_th=np.append(gamma2_th,tmp2)
    return omn,gamma1,gamma2,omn_th,gamma1_th,gamma2_th

#time,nrg1,nrg2 = get_nrg0('_beta_.274_3D')
omn,gr_1,gr_2,omn_th,th1,th2 = get_rows()

#print omn,gr_1,gr_1
#plt.plot(t,t*0.0+0.381081,'c--')
#print omn_th,th1,th2
plt.plot(omn_th,th1,'r-',markersize=8,markerfacecolor='None',label='addiabatic electron')
plt.plot(omn_th,th2,'b-',markersize=8,markerfacecolor='None',label='nonadiabatic electron')
plt.plot(omn,gr_1,'ro',markersize=8,markerfacecolor='None',label='addiabatic electron')
plt.plot(omn,gr_2,'bo',markersize=8,markerfacecolor='None',label='nonadiabatic electron')
plt.legend(loc='upper left',fontsize = 14)
plt.axis([0,40,0,6])
plt.title('$\omega_{ni}$ scan',fontsize = 20)
plt.xlabel('$\omega_{ni}$',fontsize=20)
plt.ylabel('$\gamma$',fontsize=20)
#plt.tick_params(axis = 'both', which = 'major', labelsize = 14)
#plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
plt.show()

