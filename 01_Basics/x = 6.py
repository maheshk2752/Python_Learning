#nested 
a  = int(input("enter first number:"))
b  = int(input("enter second number:"))
c  = int(input("enter third number:"))

if(a>=b and a>=c):
    print("first is largest number", a)
elif(b>=c):
    print("second is largest number", b)
else:
    print("third is largest ", c)