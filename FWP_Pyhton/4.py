import os
os.mkdir("Friends")
os.chdir("Friends")
for i in range(1,11,1):
    os.mkdir("Friend"+str(i))