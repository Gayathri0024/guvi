print("Enter a value")
a=input()
print("Enter b value")
b=input()
if((a=="rock") and (b=="paper")):
  print("b wins")
if((a=="rock") and (b=="scissors")):
  print("a wins")
if((a=="paper") and (b=="rock")):
  print("a wins")
elif((a=="paper") and (b=="scissors")):
  print("b wins")
elif((a=="scissors") and (b=="paper")):
  print("a wins")
elif((a=="scissors") and (b=="rock")):
  print("b wins")
