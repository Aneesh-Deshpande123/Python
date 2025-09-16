from django.shortcuts import render
import datetime as dt

def home(request):
    p = 10000
    t = 3
    r = 8
    si = p*t*r/100       
    a = p+si
    dt1 = dt.datetime.now()
    dt2 = dt1.strftime("%d %b %Y")
    return render(request,"app2/index.html",{"p":p, "t":t, "r":r, "a":a, "si":si, "dt":dt2})
