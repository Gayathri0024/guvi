1.	Using while loop create sum of two no with ask permission to continue or not.

i=1
while i<=4:
  a = int(input())
  b =int(input())                   
  c=a+b
  print(c)
  y=input()
  if(y=="yes"):
    continue
  else:
    break
