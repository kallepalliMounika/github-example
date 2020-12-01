#write a prgrm to calc the gcd two numbers
a=int(input("enter a number:"))
b=int(input("enter a number:"))
if a>0:
    min=a
else:
    min=b
while(min>0):
    if(a%min==0 and b%min==0):
        print("gcd is",min)
        break
    min=min-1
            
