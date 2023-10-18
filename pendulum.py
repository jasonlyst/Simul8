import math
import matplotlib.pyplot as plt
import numpy as np
import scipy as sci




c0 = np.pi*0.96
c1 = 3
n = 3000000
start = 0
stop = 25
t = np.linspace(start,stop,n+1)
vec = np.zeros([2,n+1])
#Under m type 0 , 1 , gravity*-1 , dampening constant*-1


m = np.array([[0,1],[-7,-0.2]])


#forcing function if applicable
f = np.zeros(n+1)

fmat = np.zeros([2,n+1])

fmat[1,:]=f




vec[0,0] = c0
vec[1,0] = c1
dt = ((stop-start)/n)
vec2 = np.zeros([2,n+1])
vec2[0,0] = np.sin(c0)
vec2[1,0] = c1

for i in range(n):
    dxdu = np.matmul(m,(vec2[:,i]*dt))+fmat[:,i]*dt
    vec[:,i+1] = vec[:,i] + dxdu
    vec2[0,i+1] = np.sin(vec[0,i]+dxdu[0])
    vec2[1,i+1] = vec[1,i]+dxdu[1]

x = vec[0,:]
dxdt = vec[1,:]

plt.plot(t,x)
plt.plot(t,dxdt)
plt.legend(['angle','angular velocity'])
plt.show()

