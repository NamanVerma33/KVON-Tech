n = 18
try:
   print(n)
except:
   print("Something went wrong")
else:
   print("No error")


try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")


y=5
try:
    print(y)
except:
   print("Something went wrong")
finally:
   print("This part is always excuted")
