import numpy as np
#1D array slicing
# arr=np.array([1,2,3,4,5,6,7,8,9])
# print(arr [1:5])

# arr=np.array([1,2,3,4,5,6,7,8,9])
# print(arr[:4])

#1D array negative slicing
# arr=np.array([1,2,3,4,5,6,7,8,9])
# print(arr[-3:-1])

#step
# arr=np.array([1,2,3,4,5,6,7,8,9])
# print(arr[1:6:2])

# arr=np.array([1,2,3,4,5,6,7,8,9])
# print(arr[::2])

#slicing 2D array:
#from both elements, return index 2:
# arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])
# print(arr[0: , 2])

#from both elements, slice index 1 to 4 that will return 2 dimentions.
arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[0: , 1:4])

