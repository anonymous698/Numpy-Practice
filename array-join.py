#using CONCATENATE:

import numpy as np
# arr1=np.array([1,2,3,4,5])
# arr2=np.array([6,7,8,9,10])
# arr=np.concatenate((arr1,arr2))
# print(arr)

arr1=([[1,2],[3,4]])
arr2=([[5,6],[7,8]])
arr=np. concatenate((arr1,arr2),axis=1)
print(arr)