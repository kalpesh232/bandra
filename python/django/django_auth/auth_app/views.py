from django.shortcuts import render
from .models import *

# Create your views here.
def RegisterPage(request):
    return render(request,'auth_app/register.html')

def User_Register(request):
    if request.method == 'POST':
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        user = UserRegister.objects.filter(Email = email)
        if user:
            message = 'User Alraedy Exist'
            return render(request, 'auth_app/register.html', {'msg' : message})
        else:
            if password == cpassword:
                UserRegister.objects.create(Firstname = firstname, Lastname = lastname, Email = email, Phone = phone, Password = password)
                message = 'User Successfully Created'
                return render(request, 'auth_app/login.html',{'msg':message})
            else:
                message = 'Please Check Password'
                return render(request, 'auth_app/register.html', {'msg' : message})

