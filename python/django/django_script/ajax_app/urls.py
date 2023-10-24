from django.urls import path, include
from . import views

urlpatterns = [
  path("",views.html_form,name='html_form')
]