from django.shortcuts import render

def home(request):
    p = 10000
    t = 3
    r = 8
    si = p*t*r/100       
    a = p+si
    templates = '''
Dear Chandrashekar,
You will receive an amount of Rs {r1}. on . for a deposit of Rs………  

Total Interest is ……
We are always at your service.
nqx-yfrk-fnm
    '''
