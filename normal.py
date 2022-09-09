import numpy as np
import matplotlib.pyplot as plt

for p in [(0,1),(0,2),(0,3)]:
    u, s = p
    x = np.linspace(u-3*s, u+3*s, 100)
    plt.plot(x, 1 / (np.sqrt(2 * np.pi) * s) * np.exp(-(x-u)**2 / (2 * s**2)),
             label=r'$\mu=%.1f,\ \sigma=%.1f$' % (u, s))

plt.legend()
plt.savefig('/mnt/d/normal.png')
plt.show()
