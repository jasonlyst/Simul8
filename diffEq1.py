import math
import matplotlib.pyplot as plt
import numpy as np
import scipy as sci

c = 0.1
n = 100000
start = 0
stop = 100
x = np.linspace(start,stop,n+1)
y = np.zeros(n+1)
y[0]=c

dx = ((stop-start)/n)

#model diff eq : dy/dx=sqrt(1/y) 
#This is a rough model of a projectile at escape velocity


for j in range(n):
    dy = (np.sqrt(1/y[j]-3))*dx
    y[j+1] = y[j]+dy

plt.plot(x,y)
plt.show()