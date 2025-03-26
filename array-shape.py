import numpy as np
#determining the shape of a 2D array.
# arr=np.array([[[1,2,3,5],[4,5,6,4]],[[7,8,9,4],[10,11,12,5]]])
# print(arr.shape)

arr=np.array([1,2,3,4],ndmin=8)
print(arr.shape)