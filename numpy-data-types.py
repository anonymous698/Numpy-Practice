import numpy as np
#dtype prints the datatype of an array in numpy.
# arr=np.array([1,2,3,4,5,6,7,8,9])
# print(arr.dtype)

# arr=np.array(['apple','banana','mango','watermelon','coconut'])
# print(arr.dtype)

# arr=np.array([1,2,3,4,5],dtype="S")
# print(arr)
# print(arr.dtype)

# arr=np.array([1,2,3,4,5,6],dtype="i4")
# print(arr)
# print(arr.dtype)

arr=np.array([-1,0,1])
newarr=arr.astype(bool)
print(newarr)
print(newarr.dtype)