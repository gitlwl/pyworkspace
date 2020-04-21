import numpy as np
import matplotlib.pyplot as plt

fig=plt.figure(figsize=(12,4))
ax1=fig.add_subplot(1,3,1)
ax2=fig.add_subplot(1,3,2)
ax3=fig.add_subplot(1,3,3)
ax1.plot([1,2,3])
ax2.plot([3,2,1])
ax3.plot([2,2,2])
plt.show()