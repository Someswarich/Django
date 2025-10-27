from django.shortcuts import render
from .models import Data
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def get_user(req):
    details=Data.objects.all().values()
    
    return JsonResponse({"data":list(details)})
@csrf_exempt
def reg_user(req):
    details=json.loads(req.body)
    stu_id=details.get('id')
    stu_name=details.get('name')
    stu_age=details.get('age')
    stu_department=details.get('department')
    
    existing=Data.objects.filter(id=stu_id)
    if existing.exists():
        return HttpResponse("already existed")
    else:
        detail=Data.objects.create(name=stu_name,age=stu_age,department=stu_department)
        return HttpResponse("student registered")
    
@csrf_exempt
def update_user(req,id):
     if req.method=='PATCH':
        details=json.loads(req.body)
        stu_id=details.get('id')
        stu_name=details.get('name')
        stu_age=details.get('age')
        stu_department=details.get('department')
        # stu_data=list(Data.objects.all().values())
        # print(list(stu_data))
        existing=Data.objects.filter(id=stu_id)
        existing=existing.first()
        # print(existing)
        
        if details.get('name'):
            stu_name=details['name']
              
        if details.get('age'):
            stu_age=details['age']
              
        if details.get('department'):
            stu_department=details['department']
            Data.save()
            return HttpResponse("updated succeesfully")
     else:
         return HttpResponse("student not found")



  




    
    
    

