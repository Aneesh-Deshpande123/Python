output = "NO"
year=int(input("Enter any year: "))
if year%4==0:
    output = "YE"
    if year%100==0: 
       if  year%400==0:
         output ="YE"
       else:
         output = "NO"
print(output) 