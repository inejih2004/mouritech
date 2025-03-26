from django.urls import path
from . import views
from .views import update_course, delete_course, edit_profile, add_course

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('add/', add_course, name='add_course'),
    path('update/<int:course_id>/', update_course, name='update_course'),
    path('delete/<int:course_id>/', delete_course, name='delete_course'),
    path('edit-profile/', edit_profile, name='edit_profile'),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
