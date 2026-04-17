import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-5,5,100)
y1=np.sin(x)
y2=np.cos(x)

plt.figure()

plt.plot(x,y1,color='red',linewidth=12,zorder=1)
axis=plt.gca()
axis.spines['top'].set_color('none')
axis.spines['right'].set_color('none')
axis.spines['left'].set_position('center')
axis.spines['bottom'].set_position('center')

for label in axis.get_xticklabels()+axis.get_yticklabels():
    label.set_fontsize(12)
    label.set_bbox(dict(facecolor='violet',edgecolor='none',alpha=0.3))

plt.show()