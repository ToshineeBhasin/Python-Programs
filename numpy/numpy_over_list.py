import numpy as np
import time
import sys
s = range(1000)

print("Memory occupied by list : ",sys.getsizeof(5)*len(s))

d = np.arange(1000)
print("Memory occupied by numpy : ",d.size*d.itemsize)