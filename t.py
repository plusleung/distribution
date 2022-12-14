#https://baike.baidu.com/item/t%E5%88%86%E5%B8%83/299142?fr=kg_general

import numpy as np
import matplotlib.pyplot as plt
from math import gamma
from matplotlib import ticker

def t(freedom):
    x = np.linspace(-10, 10, 1001)
    y = gamma((freedom + 1) / 2) / np.sqrt(freedom * np.pi) / gamma(freedom / 2) * (1 + x**2 / freedom) ** (-((freedom + 1) / 2))
    return x, y, np.std(y)

for freedom in [1, 2, 5]:
    x, y, s = t(freedom)
    plt.plot(x, y, label=r'$v=%d,\ \sigma=%.3f$' % (freedom, s))

plt.gca().yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1,decimals=0))

plt.legend()
plt.savefig('/mnt/d/student_t.png')
plt.show()
