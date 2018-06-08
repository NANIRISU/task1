n=range(1,10)
f=[x*1 for x in n if x%2==1]
print(f)

import numpy as np
arr=np.array(range(1,10))
a= arr[arr%2==1]
print(a)
