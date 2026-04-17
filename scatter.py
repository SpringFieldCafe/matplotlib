import numpy as np
import matplotlib.pyplot as plt

n=1024
x=np.random.normal(0,4,n)
y=np.random.normal(0,4,n)
T=np.arctan2(y,x)

plt.scatter(np.linspace(-1,1,1024),np.linspace(-1,1,1024),s=75,c=T,alpha=0.3)
plt.xlim((-1,1))
plt.xlim((-1,1))
plt.xticks=(())
plt.yticks=(())


plt.show()