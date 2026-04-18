import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np


f,((ax11,ax12),(ax21,ax22))=plt.subplots(2,2,sharex=True,sharey=True)
ax11.scatter([1,2],[1,2])
ax12.plot([1,4],[3,4])
ax21.plot(np.arange(1,10,10),np.arange(1,10,10))
ax22.plot(np.arange(0,10,10),9)
plt.tight_layout()
plt.show()