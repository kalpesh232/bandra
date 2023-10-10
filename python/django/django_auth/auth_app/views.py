from django.shortcuts import render
from .models import *

# Create your views here.
def RegisterPage(request):
    return render(request,'auth_app/register.html')

def User_Register(request):
    if request.method == 'POST':
        firstName = request.POST['fname']
        lastName = request.POST['lname']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        user = UserRegister.objects.filter(Email=email)
        if user:
            massage = 'User Already Exist'
            return render(request,'auth_app/register.html', {'msg' : massage})
        else:
            if password == cpassword:
                UserRegister.objects.create(Firstname = firstName,Lastname=lastName,Email=email,Phone=phone,Password=password)
                massage = 'User Registred Successfully'
                return render(request, 'auth_app/login.html')
            else:
                massage = 'Password doesn"t Match '
                return render(request,'auth_app/register.html', {'msg' : massage})
            
       