class my_class:
    x = 5

test = my_class()
print(test.x)

class info:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

i1 = info("Raunaq", 19, "India")
print(i1.name)
print(i1.age)
print(i1.country)