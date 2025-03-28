from django.contrib.auth.models import User
from django.db import models

class Course(models.Model):
    objects = None
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    instructor = models.CharField(max_length=100)
    image = models.ImageField(upload_to='course_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)        # Auto-timestamp

    def __str__(self):
        return self.title

class Lesson(models.Model):
    objects = None
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=255)
    content = models.TextField()
    video_url = models.URLField(blank=True, null=True)
    order = models.PositiveIntegerField(default=1)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.course.title} - {self.title}"

class UserProfile(models.Model):
    objects = None
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('admin', 'Admin'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='courses_profile')

    bio = models.TextField(blank=True, null=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')

    profile_image = models.ImageField(
        upload_to='profile_images/',
        blank=True,
        null=True,
        default='static/images/inejihimage.jpeg '
    )
    def __str__(self):
        return self.user.username