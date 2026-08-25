set1 = {"apple", "banana", "orange"}
list1 = {4, 5, 6}
set2 = {1, 2, 3}
for i in set1:
    print(i)

if "banana" in set1:
    print("Yes")

set1.add("kiwi")
print(set1)
set1.update(set2)
print(set1)
set1.update(list1)
print(set1)

set1.remove(1)
print(set1)

for i in set1:
    print(i)

myset = set1.union(set2)
print(myset)