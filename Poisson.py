import numpy as np
import matplotlib.pyplot as plt
from math import factorial
from matplotlib import ticker

r=range(21)

for p in [(3,'r'),(5,'g'),(7,'b')]:
    for k in r:
        plt.scatter(k,p[0]**k * np.exp(-p[0]) / factorial(k),color=p[1])

plt.xticks(r[::1])
plt.gca().yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1,decimals=0))

plt.savefig('/mnt/d/poisson.png')
plt.show()
