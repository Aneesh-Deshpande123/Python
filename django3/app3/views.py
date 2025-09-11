from django.shortcuts import render
from app3.forms import inputform
# Create your views here.
def home(request):
    if request.method=="POST":
        form1=inputform(request.POST)
        if form1.is_valid():
            data=form1.cleaned_data
            p = data.get("p")
            t = data.get("t")
            r = data.get("r")
            si = p*t*r/100
            amount = p+si
            return render(request, 'app3/index.html',{'param1': amount, 'param2': p})
   else:
       form1 = inputform()
   return render(request, 'app3/index.html', {'form': form1})    
    
