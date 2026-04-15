import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-3,3,50)
y=x**2
z=2*x+1

plt.figure()
plt.plot(x,y)
plt.show()

plt.figure(num=3,figsize=(5,5))
plt.plot(x,z)
plt.plot
plt.show()