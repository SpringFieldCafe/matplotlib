import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-10,20,10000)
y1=np.tan(x)
y2=1/(1+(np.e**(-x)))

plt.figure()
l1,=plt.plot(x,y2,color='violet',label='softmax')
l2,=plt.plot(x,y1,color='aqua',linewidth=2.0,linestyle='--',label='tan')
plt.legend(loc='best',labels=['aaa',"bbb"],handles=[l1,l2])
plt.ylim(-2,2)
plt.grid()
plt.show()

