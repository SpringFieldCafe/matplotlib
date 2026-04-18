import numpy as np
import matplotlib.pyplot as plt

x=np.arange(0,10,0.1)
y1=np.sin(x)
y2=np.cos(x)

fig,ax1=plt.subplots()
ax2=ax1.twinx()
ax1.plot(x,y1,'g-')
ax2.plot(x,y2,'violet')

ax1.set_xlabel('X data')
ax1.set_ylabel('Y1',color='g')
ax2.set_ylabel('Y2',color='aqua')
plt.tight_layout()
plt.show()