f = open("demo1.txt","a")

f.write("\nI am appending content")
f.close()

f = open("demo1.txt","r")
print(f.read())
f.close()

g = open("demo1.txt","w")

g.write("Delete the whole content")
g.close()

g = open("demo1.txt","r")
print("Final",g.read())
g.close()