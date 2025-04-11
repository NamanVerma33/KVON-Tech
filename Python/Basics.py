# Print hello world
print("Hello world")

#Datatypes

#int 
print("Integer Datatype")
a = 5;
print(a);
print(type(a));


#float
print("FLoat Datatype")
b = 5.5;
print(b);
print(type(b));


#string
print("String Datatype")
c = "Hello";
print(c);
print(type(c));

#bool
print("bool Datatype")
c1 = True;
print(c1);
print(type(c1));

#complex
print("Complex Datatype")
d = 1j;
print(d);
print(type(d));

#list
print("List Datatype")
e = ["A","B","C"];
print(e);
print(type(e));


#tuple
print("Tuple Datatype")
f = ("A","B","C");
print(f);
print(type(f));

#dictionary
print("Dictionary Datatype")
g = {"name":"naman","age":18};
print(g);
print(type(g))

#set
print("Set Datatype")
h = {"apple","banana"};
print(h);
print(type(h));

#range

print("Range Dataset")
i = range(6);
print(i)
print(type(i))

#Indendation is required
x = 3
if(x>2):
    print("x is bigger")

tea = "fanastic"

def tea():
    global tea
    tea = "awesome" 
    print("Tea is "+ tea);

tea();
print(tea)
