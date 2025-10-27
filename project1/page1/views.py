from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.

from django.http import HttpResponse

def addition(request):
    a = request.GET.get('a')
    b = request.GET.get('b')

    if a is None or b is None:
        return HttpResponse("Provide both a and b in URL.")

    try:
        a = int(a)
        b = int(b)
    except ValueError:
        return HttpResponse("a and b must be numbers.")

    return HttpResponse(f"Addition of both numbers is {a + b}")

# def addition(request):
#     a = request.GET.get('a')
#     b = request.GET.get('b')
#     res=a+b

#     # a=request.GET.get('a')
#     # b=request.GET.get('b')
#     return HttpResponse(f"addition of both two numbers is {res}")

