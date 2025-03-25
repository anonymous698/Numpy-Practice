import numpy as np

# arr=np.array([1,2,3,4])
# newarr=arr.copy()
# arr[0]=999
# print(arr)
# print(newarr)

# arr=np.array([1,2,3,4,5])
# x=arr.view()
# arr[0]=500
# print(arr)
# print(x)

arr=np.array([1,2,3,4,5])
newarr=arr.copy()
x=arr.view()
print(newarr.base)
print(x.base)
print(arr.base)