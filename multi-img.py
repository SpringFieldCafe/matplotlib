import matplotlib.pyplot as plt

plt.figure()

plt.subplot(3,2,1)
plt.plot([0,1],[0,1])

plt.subplot(3,2,2)
plt.plot([0,4],[-3,-1])

plt.subplot(223)
plt.plot([2,6],[-1,3])

plt.subplot(4,2,8)
plt.plot([0,1],[0,3])
plt.show()