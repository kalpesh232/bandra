from django.urls import path, include
from .  import views

urlpatterns = [
    path("",views.IndexView,name="IndexView"),
    path('form',views.FormView,name='FormView'),
    path('insert/',views.InsertData,name='insert'),
    path('showpage/',views.ShowPage,name='ShowPage')
]