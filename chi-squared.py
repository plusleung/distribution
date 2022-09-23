#https://baike.baidu.com/item/%E5%8D%A1%E6%96%B9%E5%88%86%E5%B8%83/2714796?fr=kg_general
#https://zhuanlan.zhihu.com/p/457840913

import numpy as np
import matplotlib.pyplot as plt
from math import gamma
from matplotlib import ticker

for k in [1,2,3,4,6,11]:
    x = np.arange(0.5, 15, 0.1)
    plt.plot(x, 1 / 2**(k/2) / gamma(k/2) * x**(k/2 - 1) * np.exp(-x/2),
             label=r'$k=%d$' % (k))

plt.gca().yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1,decimals=0))
    
plt.legend()
plt.savefig('/mnt/d/chi-squared.png')
plt.show()
