import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(1,100,100)
y1=x**(1/2)
y2=np.log(x//2)
x1=np.linspace(-20,20,200)
y3=np.where(x1<=0,0,x1)

plt.figure()
plt.plot(x,y1)
plt.show()
plt.plot(x,y2)
plt.show()
plt.plot(x1,y3)

ax=plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
# ax.spines['bottom'].set_position(('data',-1))
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('center'))
plt.show()