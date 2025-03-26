import numpy as np
#1D:
# arr=np.array([1,2,3,4,5])
# for i in arr:
#     print(i)

#2D
# arr=np.array([[1,2,3],[4,5,6]])
# for i in arr:
#     print(i)
#     for j in i:
#         print(j)

#3D:
# arr=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
# for i in arr:
#     print(i)
#     for j in i:
#         print(j)
#         for k in j:
#             print(k)

#using nditer():

# arr=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
# for i in np.nditer(arr):
#     print(i)

#using op_dtypes and buffered flag:

# arr=np.array([1,2,3,4,5])
# for i in np.nditer(arr,flags=["buffered"],op_dtypes=["S"]):
#     print(i)

#skipping 1 element


arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])
for i in np.nditer(arr[:,::2]):
    print(i)




