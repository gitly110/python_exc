import numpy as np


a = np.arange(10)**3
a[:6:2] = -1000
print(a)
