from django.shortcuts import render

def home(request):
    num1 = 4 
    num2 = 6
    result = calc(num1, num2)
    return render(request,'app1/index.html',{'param1':result})

def calc(n1, n2):
    sum1 = n1+n2
    dif1 = n1-n2
    list1 = []
    list1.append(sum1)
    list1.append(dif1)
    return list1

