import numpy as np
import matplotlib.pyplot as plt
import math



x=np.linspace(-5,5,100)
y=np.arctan(x)

plt.figure()
plt.plot(x,y)
ax=plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))

x0=1
y0=np.arctan(x0)
plt.scatter(x0,y0,s=30,color='blueviolet')
plt.plot([x0,x0],[y0,0],'k--',lw=2.5)
plt.plot([0,x0], [y0,y0],color='aqua',linestyle='--',lw=1)

plt.annotate(r"$arctan%s$" % y0,xy=(x0,y0),xycoords='data',xytext=(+30,-30),
            textcoords='offset points',fontsize=16,arrowprops=dict(arrowstyle='->'
            ,connectionstyle='arc3,rad=.2'))


plt.text(-3,1,r"$\ \mu\ \sigma_i\ \alpha_t $",
        fontdict={'size':5,'color':'r'})

plt.show()