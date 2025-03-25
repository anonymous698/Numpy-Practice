import numpy as np

# a=np.array(1)
# b=np.array([1,2,3])
# c=np.array([[1,2,3],[4,5,6]])
# d=np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])

# print(a.ndim)
# print(b.ndim)
# print(c.ndim)
# print(d.ndim)

# arr=np.array([1,2,3,4,5],ndmin=5)
# print(arr)
# print("domentions", arr.ndim)

#1D
# arr=np.array([1,2,3,4,5])
# print(arr[2]+arr[3])

#2D
# try:
#     arr=np.array([[1,2,3],[4,5,6]])
#     print(arr[0,1])
# except Exception:
#     print("no way you did that")

#3D
# try:
#     arr=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
#     print(arr[1,1,0])

# except Exception:
#     print("no way you did that")

#negative indexing 2D:
arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[-1,-1])