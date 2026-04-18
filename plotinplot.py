import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np

fig=plt.figure()
x=list(range(0,8))
y=[1,3,5,8,4,5,9,2]

left,bottom,width,height=0.1,0.1,0.8,0.8
ax1=fig.add_axes([left,bottom,width,height])
ax1.plot(x,y,color='violet')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('title')

left,bottom,width,height=0.2,0.3,0.3,0.3
ax2=fig.add_axes([left,bottom,width,height])
ax2.plot(y,x,color='aqua')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('title inside1')


plt.axes([.6,0.2,0.3,0.3])
plt.plot(y[::-1],x,'g')
plt.xlabel('x')
plt.ylabel('y')
plt.title('title inside2')

plt.show()