import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

plt.figure()
ax1=plt.subplot2grid((3,3),(0,0),colspan=3,rowspan=1)
ax1.plot([1,2],[1,2])
ax1.set_title('ax1-title')
ax2=plt.subplot2grid((3,3),(1,0),colspan=2,rowspan=1)
ax2.plot([3,6],[5,8])
ax3=plt.subplot2grid((3,3),(1,2),colspan=1,rowspan=2)
ax3.plot([6,9],[11,19])
ax4=plt.subplot2grid((3,3),(2,0),colspan=1,rowspan=1)
ax4.plot([3,9],[6,9])

## ax5=plt.subplot2grid((3,3),(2,1),colspan=2,rowspan=1)
# ax5.plot([3,8],[5,9])
plt.tight_layout()
plt.show()