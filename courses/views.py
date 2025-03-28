from django.shortcuts import render
from pyexpat.errors import messages

from courses.forms import UserProfileForm, LessonForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Course, UserProfile, Lesson
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
def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the course to the database
            return redirect('dashboard')  # Adjust the redirect URL accordingly
    else:
        form = CourseForm()

    return render(request, 'add_course.html', {'form': form})

def add_lesson(request, course_id):
    course = Course.objects.get(id=course_id)  # Get the course by ID
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            lesson = form.save(commit=False)
            lesson.course = course  # Assign the course to the lesson
            lesson.save()
            return redirect('dashboard')  # Redirect to the dashboard after saving
    else:
        form = LessonForm(initial={'course': course})

    return render(request, 'add_lesson.html', {'form': form, 'course': course})

def update_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = CourseForm(instance=course)
    return render(request, 'modifier_course.html', {'form': form})
def delete_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    course.delete()  # Deletes the course immediately
    return redirect('dashboard')  # Redirect to the dashboard immediately
def edit_profile(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'edit_profile.html', {'form': form})
def lesson_detail(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)

    # Fetch previous and next lessons (if they exist)
    previous_lesson = Lesson.objects.filter(course=lesson.course, order__lt=lesson.order).order_by('-order').first()
    next_lesson = Lesson.objects.filter(course=lesson.course, order__gt=lesson.order).order_by('order').first()

    return render(request, 'lesson_page.html', {
        'lesson': lesson,
        'previous_lesson': previous_lesson,
        'next_lesson': next_lesson
    })
