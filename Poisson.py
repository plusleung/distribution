import numpy as np
import matplotlib.pyplot as plt
from math import factorial

r=range(21)

for p in [(3,'r'),(5,'b'),(7,'g')]:
    for k in r:
        plt.scatter(k,p[0]**k * np.exp(-p[0]) / factorial(k),color=p[1])

plt.xticks(r[::1])
plt.savefig('/mnt/d/poisson.png')
plt.show()
