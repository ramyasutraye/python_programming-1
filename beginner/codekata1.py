#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Administrator
#
# Created:     04/02/2018
# Copyright:   (c) Administrator 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
a=input()
if(a>0 and a<100000):
    print("the value is positive")
elif(a<0):
    print("the value is negative")
elif(a==0):
    print("the value is zero")
else:
    print ("the value is invalid")



