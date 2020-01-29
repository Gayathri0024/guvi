import random
def ranfunc():
  n=random.randint(0,50)
  return n
n=ranfunc()
guess=int(input("Enter ur guess"))
print(n)
if(guess==n):
  print("You WIN")
else:
  print("You Lost")
