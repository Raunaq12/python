import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(arr.ndim) #checks the dimension of the array

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a)
# print(a.ndim)

print(arr[0])

print(arr[0:3])
print(arr[0:5:2])
print("\n")
print(a[0:3, 1])

test = "Çok güzel"
print(test.upper())