from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Student
import json

# Create your views here.
def get(req):
    student_details=Student.objects.all()
    student_details=student_details.values()
    print(list(student_details))
    # data=json.loads(req)
    return JsonResponse({"data":list(student_details)})
@csrf_exempt
def post_student(req):
    data=json.loads(req.body)
    stu_name=data.get('name')
    stu_age=data.get('age')
    stu_course=data.get('course')
    data=Student.objects.create(name=stu_name,age=stu_age,course=stu_course)
    return HttpResponse("hi")
    
