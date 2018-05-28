n=int(input())
m=int(input())
for i in range(n,m):
  if (i>1):
    for k in range(2,i):
      if (i%k)==0:
        print("the answer is:")
        break
      else:
        print(i)
        break

      
    
