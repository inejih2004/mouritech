from django.shortcuts import render
from . models import UserProfile

def dashbordEtudient(request):
    return render(request,'dashbordEtudient/dashbordEtudient.html',{'Userprofile':UserProfile.objects.all()})



