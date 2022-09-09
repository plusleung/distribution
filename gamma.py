import numpy as np
import matplotlib.pyplot as plt
from math import factorial

for p in [(1, 1), (5, 1), (10, 1), (10, 2), (10, 4)]:
    a, b = p[0], p[1]
    u, s = a/b, a**0.5/b
    x = np.arange(0, 20, 0.1)
    plt.plot(x, b**a / factorial(a-1) * (x**(a-1)) * np.exp(-b*x), 
             label=r'$\alpha=%d,\ \beta=%.1f,\ \mu=%.1f,\ \sigma=%.1f$' % (a, b, u, s))

plt.legend()
plt.savefig('/mnt/d/gamma.png')
plt.show()
