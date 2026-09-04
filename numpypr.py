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

x = arr.copy()
print(x)
y = arr.view()
y[0] = 10
print(y)
print(arr)
print(a.shape)
z = a.reshape(-1)
print(z)
print(a)

new_arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
for i in new_arr:
    print(i, end=" ")
print("\n")
for i in a:
    for j in i:
        print(j, end=" ")

for i in np.nditer(a): #nditer is a iterator which makes iterating through 2d and 3d arrays easier
    print(i) 

a_arr = np.array([1, 2, 3])
b_arr = np.array([4, 5, 6])
c_arr = np.concatenate((a_arr, b_arr))
print(c_arr)
d_arr = np.stack((a_arr, b_arr))
print(d_arr)
e_arr = np.split(a_arr, 3)
print(e_arr)

print(np.where(a_arr == 2))

sort1 = np.array([7, 3, 1, 8, 4, 9])
print(np.sort(sort1))