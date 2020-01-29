def nano():                            
  a=int(input())                         
  b=int(input())
  kms=a+b                     
  cost=kms*100
  print("kms =",kms)
  print("cost =",cost)
def micro():
   a=int(input())
   b=int(input())
   kms=a+b
   print("kms =",kms)
def prime():
   a=int(input())
   b=int(input())
   kms=a+b
   print("kms =",kms)
e=input()
d={'nano':nano(),'micro':micro(),'prime':prime()}
if e=="nano":
  d.nano()
elif e=="micro":
  d.micro()
elif e=="prime":
  d.prime()
