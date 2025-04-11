f = open("newFile.txt","w")

f.write("Hello")

f = open("newFile.txt","r")
print(f.read())
f.close()

g = open("newFile.txt","w")
g.write("Hello 1")

g = open("newFile.txt","r")
print(g.read())
g.close()