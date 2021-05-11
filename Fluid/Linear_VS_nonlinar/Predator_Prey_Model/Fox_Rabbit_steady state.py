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
tot_steps=5000           #total steps of time

#\frac{d x_i}{dt} = a_i x_i + \sum_{j} b_{ij} x_i x_j

x=[0.]*num_mod
a=[0.]*num_mod
b=np.zeros((num_mod,num_mod))

label_list=['fox', 'rabbit']

case_number= -1 #case1


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

if case_number==1:
    # x[0]=number of Fox
    # x[1]=number of Rabbit
    x[0]=0.01
    x[1]=0.01

    #natural growth rate for fox(0) and rabbit(1)
    a[0]=-0.02   #growth rate for fox
    a[1]= 0.02   #growth rate for rabbit

    #interaction of fox and rabbit
    b[0,0]=-0.0         #impact to fox    of interaction of fox    and fox    (internal competetion)
    b[0,1]= 0.2          #impact to fox    of interaction of fox    and rabbit (fox eats rabbit and grow fater)
    b[1,1]=-0.0         #impact to rabbit of interaction of rabbit and rabbit (internal competetion)
    b[1,0]=-0.3           #impact to rabbit of interaction of fox    and rabbit (rabbit eateb by fox and grow slower)



print('a:'+str(a))
print('b:'+str(b))

#For steady state, d/dt=0