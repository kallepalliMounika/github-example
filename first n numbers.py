#write a prgrm to calc the average of first n numbers
n=int(input("enter a number:"))
sum=0
for i in range (n+1):
    sum=sum+i
    a=sum/n
print("the average of first ",n,"natural numbers is",a)

