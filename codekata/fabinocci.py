n = int(input("enter the input value:"))
n1 = 0
n2 = 1
count = 0
if n<= 0:
   print("Please enter a positive integer")

else:
     print("Fibonacci sequence:")
     for i in range(0,n):
       print(n1,end=',')
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1
       
