n=int(input())
temp=n
rev=0
while(n>0):
    m=n%10
    rev=rev*10+m
    n=n//10
if(temp==rev):
    print("The number is a palindrome")
else:
    print("The number not a palindrome")
