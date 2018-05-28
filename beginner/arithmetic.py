a=float(input())
b=float(input())
choice=float(input())
if((choice>=1 and choice<=1.9)):
  c=a+b
  print("the addition of two numbers")
  print(c)

elif(choice==2):
  d=a-b
  print("the subration of two numbers")
  print(d)

elif(choice==3):
  e=a*b
  print("the multiplication of two numbers")
  print("{:.2f}".format(e))

elif(choice==4):
  f=a%b
  print("the modulo of two numbers")
  print(f)

elif(choice==5):
  g=a**b
  print("the power of two numbers")
  print(g)

elif(choice==6):
  if(b==0):
    print("infinity")
  else:
    h=a/b
    print("the division of two numbers")
    print(h)
   
else:
  i=a**b
  print("the exponential of two numbers",i)




  





