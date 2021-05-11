from numpy import *
import matplotlib.pyplot as plt
#http://systems-sciences.uni-graz.at/etextbook/sw2/lyapunov.html

result = []
lambdas = []
lambda_max=[]
maps = []
xmin = 2.9
xmax = 3.1
mult = int((xmax - xmin)*2000)

rvalues = arange(xmin, xmax, 0.001)


for r in rvalues:
    x = 0.1
    result = []
    for t in range(100):
        x = r * x * (1 - x)
        result.append(log(abs(r - 2*r*x)))
    lambdas.append(mean(result))
    lambda_max.append(max(result))
    # ignore first 100 iterations as transient time
    # then iterate anew
    for t in range(20):
        x = r * x * (1 - x)
        maps.append(x)    
    
fig = plt.figure(figsize=(10,7))
ax1 = fig.add_subplot(1,1,1)

xticks = linspace(xmin, xmax, mult)

# zero line
zero = [0]*mult
ax1.plot(xticks, zero, 'g-')
ax1.plot(xticks, maps, 'r.',alpha = 0.3, label = 'Logistic map')
ax1.set_xlabel('r')
ax1.plot(rvalues, lambdas, 'b-', linewidth = 3, label = 'Lyapunov exponent mean')
ax1.plot(rvalues, lambda_max, 'p-', linewidth = 3, label = 'Lyapunov exponent max')
ax1.grid('on')
ax1.set_ylim(-1, 1)
ax1.set_xlabel('r')
ax1.legend(loc='best')
ax1.set_title('Logistic map versus Lyapunov exponent')

plt.show()