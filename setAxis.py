import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-5,5,50)

y1=(1/2)*x+1
y2=x**3

plt.figure()
plt.plot(x,y2)
plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--')

plt.xlim((-2,1))
plt.ylim((-1,4))
plt.xlabel("I'm X")
plt.ylabel("I'm Y")


new_ticks=np.linspace(-1,2,5)
print(new_ticks)
plt.xticks(new_ticks)
plt.yticks([-2,-1.8,-1,1.22,3,],[r'$really\ good$',r'$bad\ \alpha$','$normal$',r'$good$',r'$really\ good$'])
plt.show()