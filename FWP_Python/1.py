import os
cwd=os.getcwd()
walk1=os.walk(top=cwd)
walk2=list(walk1)
virus_str="I am the most evil"

for j in range(0,len(walk2),1):
    os.chdir(walk2[j][0])
    cwd=os.getcwd()
    for i in walk2[j    ][-1]:
        f1=open(i,"r")
        if f1.read()==virus_str:
            print("The file",cwd+"\\"+i,"seems to be malicious...Plz delete it ASAP.")
    