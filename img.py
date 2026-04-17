import numpy as np
import matplotlib.pyplot as plt

a=np.array(np.random.rand(3,3))

plt.imshow(a,interpolation='nearest',cmap='spring',origin='upper')
plt.colorbar(shrink=0.8)

plt.xticks(())
plt.yticks(())
plt.show()