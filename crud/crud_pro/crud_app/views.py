from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from crud_app.models import Emp_data

# Create your views here.

def get_user(req):
    data=Emp_data.objects.all() #to fetch all the records from the db and 
    #the data is in querset binary form so using orm values method we convert it as a dictionaries
    # print(data)
    details=data.values()
    # print(details)
    #print(details) it converts as dictionary but we have to display in browser 
    # #we need convert as python lists
   
    return JsonResponse({"Emp_details":list(details)})
@csrf_exempt
def reg_user(req):
    data=json.loads(req.body)
    emp_name=data.get('name')
    emp_salary=data.get('salary')
    emp_role=data.get('role')
    emp_id=data.get('id')
    existing_emp = Emp_data.objects.filter(id=emp_id)
    if existing_emp.exists():
        return HttpResponse("Employee already exists")
        
    else:
        table=Emp_data.objects.create(name=emp_name,salary=emp_salary,role=emp_role)
        return HttpResponse("emp registered successfully")


@csrf_exempt
def update_user(req,id):
    if req.method=='POST':
        data=json.loads(req.body)
        emp_id=data.get('id')
        emp=Emp_data.objects.filter(id=id)
        # print(Emp_data.objects.all().values())
        # print(Emp_data.objects.filter(id=2).exists())
        if emp.exists():
              emp = emp.first()
              if data.get('name'):
                emp.name = data['name']
              if data.get('salary'):
                emp.salary = data['salary']
              if data.get('role'):
                emp.role = data['role']

              emp.save()
              return HttpResponse("Employee updated successfully")
        else:
            return HttpResponse("Employee not found")
        
    