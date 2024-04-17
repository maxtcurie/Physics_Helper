import numpy as np
import matplotlib.pyplot as plt
import math

#5 white ball 1-69
#1 red   ball 1-26

#Jackpot=10**9 #assume jackpot it 1b

def reward_cal(Jackpot):
             #[0,1,2,3,4,  5  ]
    reward5  =[0,0,0,7,100,100000] #reward for getting white call from 0 to 5
             #[0,1,2,3,4,  5  ]
    reward5n1=[4,4,7,100,50000,Jackpot] #reward for getting 

    probability=[math.comb(5, i)*math.comb(64, 5-i)/math.comb(69, 5) for i in range(6)]

    reward5=np.array(reward5)
    reward5n1=np.array(reward5n1)
    probability=np.array(probability)

    Ex_reward=probability*reward5*25/26
    Ex_reward5n1=probability*reward5n1*1/26
    return np.sum(Ex_reward+Ex_reward5n1)

Ex=[]
Jackpot_list=np.linspace(0.1,2.,20)*10**9
for Jackpot in Jackpot_list:
    Ex.append(reward_cal(Jackpot))

plt.clf()
plt.plot(Jackpot_list,Ex)
plt.axhline(2,color='red')
plt.show()