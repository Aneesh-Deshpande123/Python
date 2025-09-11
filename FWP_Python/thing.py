import time
up_down=input("Up or down? ")
num=int(input("Enter number(highest is 10th floor) "))
if up_down=="up":
    if num>10:
        print("you're going out of the building!!")
    else:
        for i in range(1,num+1):
            print(i)
            time.sleep(2)
    print("You're at floor:",num)
if up_down=="down":
     for r in range(10,num,-1):
        print(r)
        time.sleep(2)
     print("You're at floor:",num)
if up_down != "up" or up_down != "down":
    print("no")
    print()
