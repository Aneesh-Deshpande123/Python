num1=int(input("Enter number "))
num2=int(input("Enter number2 "))
num3=int(input("Enter number3 "))
if num1==num2==num3:
    print("no")
if num1-num2>0 and num1-num3>0:
    print(num3)
if num2-num1>0 and num2-num3>0:
    print(num3)
if num3-1>0 and num3-num2>0:
    print(num3)