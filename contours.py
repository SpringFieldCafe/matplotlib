import numpy as np
import matplotlib.pyplot as plt

def f(x,y):
    return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)

n=256
x=np.linspace(-3,3,n)
y=np.linspace(-3,3,n)

x,y=np.meshgrid(x,y)
plt.contourf(x,y,f(x,y),10,alpha=0.72,cmap='cool')
c=plt.contour(x,y,f(x,y),10,colors='black',linewidth=1)

plt.clabel(c,inline=True,fontsize=10)

plt.xticks(())
plt.yticks(())
plt.show()