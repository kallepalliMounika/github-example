#write a prgrm to print the all leap years from 1900-2101

for i in range (1900,2101):
    if ((i%4==0 or i%400==0) and i%100!=0):
        print(i)
        
