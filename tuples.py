tuple1 = ("apple", "banana", "orange")
print(tuple1)
for i in range(len(tuple1)):
    print(tuple1[i])
print("\n")
for i in tuple1:
    print(i)

print(len(tuple1))

list1 = list(tuple1)
list1[0] = "kiwi"
tuple1 = tuple(list1)
print(tuple1)

(a, *b) = tuple1
print(b)