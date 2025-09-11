import random
import time #time for more realizim.
input1=input("Which bank are you(BOA, Chase, Us Bank, or Wells Fargo)? ")
otp=0

if input1=="BOA":
    otp=random.randint(1000,9999)
    print(otp)

elif input1=="Chase":
    otp=random.randint(100,999)
    print(otp)

elif input1=="Us Bank":
    otp=random.randint(100000,999999)
    print(otp)
 
elif input1=="Wells Fargo":
    otp=random.randint(1000000000,9999999999)
    print(otp)

for i in range(3,0,-1):
    time.sleep(2)
    input_otp=int(input("Enter otp "))
    
    if input_otp==otp:
        print("You have logged in to your account")
        quit()
    else:
        print("Access denied.", i-1," attempts remain.")

    if i==1:
        str = "Account forzen. Please contact www." + input1.strip() + ".com"
        print(str)