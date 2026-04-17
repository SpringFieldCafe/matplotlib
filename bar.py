import numpy as np
import matplotlib.pyplot as plt

n=12
x=np.arange(n)
y1=(1-x/float(n))*np.random.uniform(0.5,1,n)
y2=(1-x/float(n))*np.random.uniform(0.5,1,n)

plt.bar(x,+y1,facecolor=(0,0.5,0),edgecolor='white')
plt.bar(x,-y2,facecolor='violet',edgecolor='black')

for a,b in zip(x,y1):
    plt.text(a,b,'%.2f' % b,ha='center',va='bottom')


for x,y in zip(x,y2):
    plt.text(x,-y-0.05,'-%.2f' % y,ha='center',va='top')

plt.xlim(-.5,n)
plt.xticks(())
plt.ylim(-1.25,1.25)
plt.yticks(())
plt.show()