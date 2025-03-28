from django import forms
from .models import Course, UserProfile,Lesson
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'category', 'duration', 'instructor', 'image']

    def __init__(self, *args, **kwargs):
            super(CourseForm, self).__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.widget.attrs.update({
                    'class': 'form-control'
                })
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_image', 'bio', 'role']

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['course', 'title', 'content', 'video_url', 'order', 'is_published']

    course = forms.ModelChoiceField(queryset=Course.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    title = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    video_url = forms.URLField(required=False, widget=forms.URLInput(attrs={'class': 'form-control'}))
    order = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    is_published = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
