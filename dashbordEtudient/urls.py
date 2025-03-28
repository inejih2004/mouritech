from django.urls import path
from . import views


urlpatterns = [
     path('dashbordEtudient',views.dashbordEtudient,name='dashbordEtudient')
     
]