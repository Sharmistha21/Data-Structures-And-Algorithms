import numpy as np

arr=np.array([1,2,3])
print(arr)

arr=np.array([[1,2,3],
             [4,5,6]])
print(arr)

arr=np.array((1,3,2))
print(arr)

arr = np.array([[-1, 2, 0, 4],
                [4, -0.5, 6, 0],
                [2.6, 0, 7, 8],
                [3, -7, 4, 2.0]])

arr1=arr[:2,::2]
print(arr1)

arr2=arr[[1,1,0,3],[3,2,1,0]]
print(arr2)

a=np.array([[1,2],
            [3,4]])

b=np.array([[4,3],
            [2,1]])

print("add 1 to each element of a:", a+1)
print("Subtract 2 from each element of b:",b-2)
print("sum of all array elements:",a.sum())
print("\narray sum:\n",a+b)

x=np.array([1,2])
print(x.dtype)

x=np.array([1.0,2.0])
print(x.dtype)

x=np.array([1,2],dtype=np.int64)
print(x.dtype)


