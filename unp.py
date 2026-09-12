import numpy as np
# x = [1, 2, 3, 4]
# y = [5, 6, 7, 8]
# z = np.add(x, y)
# print(z)

def add(x, y):
    return x+y

add = np.frompyfunc(add, 2, 1) #python upy function
print(add([1, 2, 3, 4], [5, 6, 7, 8]))
print(type(add))

if type(np.add) == np.ufunc:
    print("np is a ufunction")

a = [9, 10, 11, 12]
b = [13, 14, 15, 16]
print(np.add(a, b))
print(np.subtract(a, b))
print(np.subtract(b, a))
print(np.multiply(a, b))
print(np.divide(a, b))
print(np.power(a, b))
print(np.mod(a, b))
c = np.subtract(a, b)
print(np.absolute(c))