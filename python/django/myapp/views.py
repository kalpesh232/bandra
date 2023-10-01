from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def IndexView(request):
    return render(request, 'myapp/index.html')

def FormView(request):
    return render(request,'myapp/form.html')

def InsertData(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    contact = request.POST['contact']

    newuser = Student.objects.create(Firstname = fname, Lastname = lname, Email = email, Contact = contact)

    return redirect('ShowPage')

def ShowPage(request):
    all_user = Student.objects.all()
    print('all_user : ',all_user)
    return render(request, 'myapp/show.html',{'key1':all_user})
