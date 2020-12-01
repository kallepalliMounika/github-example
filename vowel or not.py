#write a prgrm to find the largest number in 3 digits
a=float(input("enter a number:"))
b=float(input("enter a number:"))
c=float(input("enter a number:"))
if (a>b and a>c):
    print(a,"is big")
elif (b>c):
    print(b,"is big")
else:
    print(c,"is big")
