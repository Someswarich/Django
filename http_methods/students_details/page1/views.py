from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
student=[{
    "id":1,
    "name":"sowmya",
    "place":"Guntur"
    },

    {"id":2,
    "name":"neelu",
    "place":"ndg"
    }]

@csrf_exempt
def details(req):
    
    if req.method=="POST":
        a=json.loads(req.body)
        
        for s in student:
            if s["id"]==a["id"]:
                print(s["id"],a["id"])
                return JsonResponse({"student":"already existed"})
        student.append(a)
        return JsonResponse({"message":"user registered successfully"})
      
    return JsonResponse({"user Details":student})



    
    
        
