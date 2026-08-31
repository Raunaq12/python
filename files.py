import os
f = open('demofile.txt')
print(f.read())
f.close()
print("\n")
with open('demofile.txt') as f1:
    print(f1.read())
print("\n")
with open('demofile.txt') as f2:
    print(f2.read(5))
print("\n")
with open('demofile.txt') as f3:
    print(f3.readline())
print("\n")
with open('demofile.txt') as f4:
    for x in f4:
        print(x)

with open('demofile.txt', 'a') as f:
    print(f.write("\nNow the files has more content!"))

with open('demofile.txt') as f:
    print(f.read())
print("\n")
with open("demofile.txt", "w") as f:
  f.write("Woops! I have deleted the content!")

with open("demofile.txt") as f:
  print(f.read())

f = open('myfile.txt', 'x')
f.close()

