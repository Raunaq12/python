list1 = ["apple", "banana", "cherry"]
print(len(list1))
print(list1)
if "apple" in list1:
    print("Yes it is present")

for i in range(len(list1)):
    print(list1[i])

for x in list1:
    print(x)

for i in range(1, 11):
    print(i)

[print(x) for x in list1]
newlist = [x for x in list1 if "a" in x]
print(newlist)


#list methods

list = ["a", "b", "c"]
list.append("d") #adds element to end of list
print(list)
names = list.copy() #returns copy of the list
print(names)
print(list.count("a")) #returns occurence of entered element
print(list.index("a")) #returns index of the entered element
list.insert(1, "e") #inserts element at certain index
print(list)
list.pop(1) #removes element at certain index
print(list)
list.remove("d") #removes certain element
print(list)
list.sort()#sorts the list
print(list)