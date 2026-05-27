import matplotlib.pyplot as plt
import math
from math import*
t=0
dt=0.05
g=9.8
v0=float(input("type initial velocity"))
theta =float(input("type angle"))
theta=math.radians(theta)
vx=v0 *cos(theta)
y=v0*sin(theta)*t -0.5*g*t**2
x=v0 * cos(theta)*t
t_values=[]
y_values=[]
x_values=[]
vy_values=[]

while y>=0:
    t=t+dt
    vy=v0 *sin(theta)- g*t
    y=v0*sin(theta)*t - 0.5*g*t**2
    x=x+vx
    t_values.append(t)
    x_values.append(x)
    y_values.append(y)
    vy_values.append(vy)
    
    print("y=",y, "x=",x)

if len(x_values)==0 or len(y_values)==0:
    print("empty")
    exit()


plt.figure()

plt.xlim(0,max(x_values))
plt.ylim(0,max(y_values))

plt.plot(x_values,y_values)

plt.xlabel("x")
plt.ylabel("y")

plt.xlim(0,max(x_values))
plt.ylim(0,max(y_values))


plt.grid()

plt.show()



