import numpy as np
#  CONVERTING 1D ARRAY TO A MILTI-DIMENTIONAL ARRAY
# arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# newarr=arr.reshape(2,2,3)
# print(newarr)

# arr=np.array([1,2,3,4,5,6,7,8])
# newarr=arr.reshape(2,2,-1)
# print(newarr)

#CONVERTING MULTI-DIMENTIONAL ARRAY TO A ONE DIMENTIONAL ARRAY.

arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])
newarr=arr.reshape(-1)
print(newarr)