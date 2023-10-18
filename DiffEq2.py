import math
import matplotlib.pyplot as plt
import numpy as np
import scipy as sci




c0 = 5
c1 = 0
n = 500000
start = 0
stop = 15
t = np.linspace(start,stop,n+1)
vec = np.zeros([2,n+1])
#Under m type 0 , 1 , spring constant*-1 , dampening constant*-1


m = np.array([[0,1],[-1,-0.07]])


#forcing function if applicable
f = 2*np.sin(5*t)

fmat = np.zeros([2,n+1])

fmat[1,:]=f




vec[0,0] = c0
vec[1,0] = c1
dt = ((stop-start)/n)

for i in range(n):
    dxdu = np.matmul(m,(vec[:,i]*dt))+fmat[:,i]*dt
    vec[:,i+1] = vec[:,i] + dxdu

x = vec[0,:]
dxdt = vec[1,:]

plt.plot(t,x)
plt.plot(t,dxdt)
plt.legend(['position','velocity'])
plt.show()