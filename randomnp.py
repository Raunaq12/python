import numpy as np
from numpy import random

x = random.rand() # returns a float value between 0 and 1
print(x)

y = random.randint(100, size=(5))  # for integers
print(y)

z = random.randint(100, size=(5, 5))
print(z)

a = random.rand(5)
print(a)

b = random.rand(5, 3)
print(b)

c = random.choice(y)
print(c)