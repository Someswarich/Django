from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def multiply(request):
    a=request.GET.get('a')
    b=request.GET.get('b')
    if a is None or  b is None:
        return HttpResponse("provide a and b in URL")
    
    try:
        a=int(a)
        b=int(b)
    except ValueError:
        return HttpResponse("a and b must be numbers") 
    return HttpResponse(f"Multiplication of {a} and {b} is {a*b}")
        

