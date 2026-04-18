import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec

plt.figure()
gs=gridspec.GridSpec(3,3)
ax1=plt.subplot(gs[0,:])
ax1.plot([3,7],[2,9])
ax2=plt.subplot(gs[1:3,0:2])
ax2.plot(np.linspace(1,10,10),np.linspace(4,10,10))
ax3=plt.subplot(gs[1,2])
ax4=plt.subplot(gs[2,2])

plt.tight_layout()
plt.show()