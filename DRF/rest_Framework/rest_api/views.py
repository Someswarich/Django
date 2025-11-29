
from django.http import HttpResponse
from .models import Users
from .serializers import UserSerializer
from django.shortcuts import render,redirect



# Create your views here.
def get(req):
    users_data=Users.objects.all()
    print(users_data)
    context={
        'users_data':users_data 
        }
    return render(req,"index.html",context)
def add(req):
    if req.method=="POST":
        name=req.POST.get("user_name")
        email=req.POST.get("user_email")
        mobile_no=req.POST.get("mobile_no")
        users_data=Users.objects.create(user_name=name,user_email=email,mobile_no=mobile_no)
        users_data.save()
        print(users_data)
        return redirect('get')
    return render('get')
def update(request, user_id):
    try:
        user = Users.objects.get(id=user_id)
    except Users.DoesNotExist:
        return HttpResponse("User not found")

    if request.method == "POST":
        user.user_name = request.POST.get("user_name")
        user.user_email = request.POST.get("user_email")
        user.mobile_no = request.POST.get("mobile_no")
        user.save()
        return redirect('get')
    users_data = Users.objects.all()

    return render(request, "index.html", {"user": user,
        "users_data": users_data})
def delete(req, user_id):
    user = Users.objects.get(id=user_id)
    user.delete()
    return redirect('get')


        
       
        
        
        
    
    
    
    
