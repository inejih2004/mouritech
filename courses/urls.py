from django.urls import path
from . import views
from .views import dashboard, add_course, add_lesson, update_course, delete_course, edit_profile, lesson_detail

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('add_course/', views.add_course, name='add_course'),
    path('add_lesson/<int:course_id>/', views.add_lesson, name='add_lesson'),
    path('modifier/<int:course_id>/', views.update_course, name='modifier_course'),
    path('suprimer/<int:course_id>/', views.delete_course, name='suprimer_course'),
    path('edit-profile/', edit_profile, name='edit_profile'),
    path('lesson/<int:lesson_id>/', lesson_detail, name='lesson_detail'),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
