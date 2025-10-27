from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import users
from django.views.decorators.csrf import csrf_exempt
import json

def validate_file(file):
    max_size=5*1024*1024
    if file.size>max_size:
        return False,'file size is exceeded'
    allowed_type=['image/png','image.jpg','application/pdf']
    if file.content_type not in allowed_type:
        return False,'file with jpg,png,pdf extensions only allowed'
    return True,'valid'
def validate_phn(user_mobile):
    if len(user_mobile)==10 and user_mobile.isdigit() and user_mobile[0] in ['9','6','7','8']:
        return True,'it is a indian number'
    return False,'it is not a indian number'
# Create your views here.
@csrf_exempt
def reg_user(req):
    user_name=req.POST.get('name')
    user_email=req.POST.get('email')
    user_mobile=req.POST.get('mobile')
    file=req.FILES['document']
    is_mobile_valid, mobile_msg = validate_phn(user_mobile)
    is_valid,msg=validate_file(file)
    # print(is_mobile_valid,mobile_msg)
    # print(is_valid,msg)
    if is_mobile_valid:
        pass
    else:
        return HttpResponse(mobile_msg)
    if is_valid:
        pass
    else:
        return HttpResponse(msg)
    data=users.objects.create(name=user_name,email=user_email,mobile=user_mobile,document=file)
    return HttpResponse('regestered successfully')


        
    








