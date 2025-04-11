f = open("demofile.txt")

print("Whole file read\n"+f.read())

print("Reading line by line")

f.close()


g = open("demo1.txt")
print(g.readline())
print(g.readline())
g.close()

print("Looping")
f = open("demofile.txt")

for x in f:
    print(x)