import matplotlib.pyplot as plt
import pandas as pd


#cd .\Fluid\Linear_VS_nonlinar\Predator_Prey_Model
#python 0food_chain_plot.py

num_mod=2

path='./'

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
