#https://baike.baidu.com/item/t%E5%88%86%E5%B8%83/299142?fr=kg_general

import numpy as np
import matplotlib.pyplot as plt
from math import gamma

def t(freedom):
    x = np.linspace(-6, 6, 1001)
    y = gamma((freedom + 1) / 2) / np.sqrt(freedom * np.pi) / gamma(freedom / 2) * (1 + x**2 / freedom) ** (-((freedom + 1) / 2))
    return x, y, np.mean(y), np.std(y)

for freedom in [1, 2, 5]:
    x, y, u, s = t(freedom)
    plt.plot(x, y, label=r'$v=%d,\ \mu=%.3f,\ \sigma=%.3f$' % (freedom, u, s))

plt.legend()
plt.savefig('/mnt/d/student_t.png')
plt.show()
