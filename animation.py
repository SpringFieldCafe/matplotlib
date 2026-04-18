import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation as ani

fig,ax=plt.subplots()

x=np.arange(0,2*np.pi,0.01)
line,=ax.plot(x,np.sin(x))

def anim(i):
    line.set_ydata(np.sin(x+i/100))
    return line,

def ini():
    line.set_ydata(np.sin(x))
    return line,

animation=ani.FuncAnimation(fig=fig,func=anim,frames=120,init_func=ini,interval=20,blit=True)
plt.show()