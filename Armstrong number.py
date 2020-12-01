#write a prgrm to find the armstrong number
num=int(input("enter a number:"))
sum=0
temp=num
while temp >0:
    digit = temp %10
    sum+=digit
    temp//=10
print(sum)
