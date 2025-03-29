from django.urls import path
from . import views


urlpatterns = [
    path('singup',views.singup,name='singup'),
    path('login',views.loginPage,name='login'),
]