import numpy as np
import matplotlib.pyplot as plt

#*******start of user block**************
x_init=0.1
r_min=2.9
r_max=3.1
r_step=0.001
x_min=0
x_max=1
x_step=0.01

total_steps=1000
def map_function(x,r):
	return r * x * (1 - x)
#*******end of user block**************


r_list=np.arange(r_min,r_max,r_step)
x_init_list=np.arange(x_min,x_max,x_step)
maps=[]

lambda_max_list1=[]
lambda_max_list2=[]

for x_init in x_init_list:
	print('x_init='+str(x_init))
	lambda_avg=[]
	lambda_max=[]
	for r in r_list:
		#print('r='+str(r))
		x=x_init
		lambda_list=[]
		for i in range(total_steps):
			#print('i='+str(i))
			x=map_function(x,r)
			maps.append(x)
			lambda_list.append(np.log(abs(r - 2*r*x)))
		lambda_avg.append(np.mean(lambda_list))
		lambda_max.append(np.max(lambda_list))
	r0=1.98
	lambda_max0=lambda_max[np.argmin(abs(r_list-r0))]
	print('At r='+str(r0)+', The maximum of lambda is '+str(lambda_max0))
	lambda_max_list1.append(lambda_max0)

	r0=2.03
	lambda_max0=lambda_max[np.argmin(abs(r_list-r0))]
	print('At r='+str(r0)+', The maximum of lambda is '+str(lambda_max0))
	lambda_max_list2.append(lambda_max0)
	
'''
xticks = np.linspace(r_min, r_max, len(maps))

plt.clf()
plt.plot(r_list,lambda_avg,'r.',label="lambda avg")
plt.plot(r_list,lambda_max,'b.',label="lambda max")
plt.plot(xticks,maps,'g.',alpha=0.3,label="maps")
plt.xlabel('r')
plt.grid('on')
plt.legend(loc='best')
plt.show()
'''

plt.clf()
plt.plot(x_init_list,lambda_max_list1,'r.',label="r0=1.98")
plt.plot(x_init_list,lambda_max_list2,'b.',label="r0=2.03")
plt.xlabel('initial x')
plt.ylabel('maximum of lambda')
plt.grid('on')
plt.legend(loc='best')
plt.show()

