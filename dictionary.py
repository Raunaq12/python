thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for i in thisdict.keys():
    print(i)

for i in thisdict.items():
    print(i)

thisdict.update({"year": 2000})
print(thisdict)

thisdict["color"] = "blue"
print(thisdict)

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

for i, j in myfamily.items():
    print(i)

    for obj in j:
        print(f"{obj} : {j[obj]}")

