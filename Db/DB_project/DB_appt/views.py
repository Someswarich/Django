from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Employee,Student

import json

# Create your views here.
@csrf_exempt
def employee(request):
    if (request.method=="POST"):
         data=json.loads(request.body)
         first_name = data.get('first_name')
         last_name = data.get('last_name')
         department = data.get('department')
         details=Employee.objects.create(first_name=first_name,last_name=last_name,department=department)
         print(details)

         return JsonResponse({"data":"entered details"})
    employees = list(Employee.objects.values())
    return JsonResponse({"employees": employees})



@csrf_exempt
def student_data(request):
    if request.method=="POST":
         val=json.loads(request.body)
         first_name = val.get('first_name')
         last_name = val.get('last_name')
         age = val.get('age')
         roll_number = val.get('roll_number')

         details=Student.objects.create(first_name=first_name,last_name=last_name,age=age,roll_number=roll_number)
         print(details)

         return JsonResponse({"data":"entered details"})
    values = list(Student.objects.values())
    return JsonResponse({"students": "not entered"})





    


