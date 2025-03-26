from django.shortcuts import render

from courses.forms import UserProfileForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Course, UserProfile
from .forms import CourseForm

def dashboard(request):
        courses = Course.objects.all()
        user_profile, created = UserProfile.objects.get_or_create(user=request.user)
        form = CourseForm()
        return render(request, 'dashboard.html', {
            'courses': courses,
            'user_profile': user_profile,
            'form': form
        })

    # Add Course View

def add_course(request):
        if request.method == 'POST':
            form = CourseForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('dashboard')
        return redirect('dashboard')

    # Update Course View

def update_course(request, course_id):
        course = get_object_or_404(Course, id=course_id)
        if request.method == 'POST':
            form = CourseForm(request.POST, request.FILES, instance=course)
            if form.is_valid():
                form.save()
                return redirect('dashboard')
        return render(request, 'update_course.html', {'form': CourseForm(instance=course)})

    # Delete Course View

def delete_course(request, course_id):
        course = get_object_or_404(Course, id=course_id)
        if request.method == 'POST':
            course.delete()
            return redirect('dashboard')
        return render(request, 'delete_course.html', {'course': course})

    # Edit Profile View

def edit_profile(request):
        user_profile, created = UserProfile.objects.get_or_create(user=request.user)
        if request.method == 'POST':
            form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
            if form.is_valid():
                form.save()
                return redirect('dashboard')
        else:
            form = UserProfileForm(instance=user_profile)
        return render(request, 'edit_profile.html', {'form': form})
