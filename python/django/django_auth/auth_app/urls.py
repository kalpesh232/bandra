from django.urls import path, include
from . import views

urlpatterns = [
   path('', views.RegisterPage, name='registerpage' ),
   path('register_user', views.User_Register, name='userregister'),
   path('login', views.LoginForm, name='login'),
   path('userlogin', views.UserLogin, name='userlogin')
]