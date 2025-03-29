from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label ='email',
        widget = forms.EmailInput(attrs= {'class':'form-control'})
    )
    username = forms.CharField(
        label='name',
        widget = forms.TextInput(attrs = {'class': 'form-control'}),
    )
    password1 = forms.CharField(
        label= 'password',
        strip = False,
        widget = forms.PasswordInput(attrs={'autocmplete':'new-password','class': 'form-control'}),
    )
    password2 = forms.CharField(
        label = "confirme password",
        strip = False,
        widget =forms.PasswordInput(attrs = {'autocmplete':'new-password','class': 'form-control'})
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields =  UserCreationForm.Meta.fields + ('email','username','password1','password2')

    def clean_email(self):
        email =self.cleaned_data.get('email')
        user_count =User.objects.filter(email=email).count()
        if user_count > 0:
            raise forms.ValidationError('email deja exist')
        return email











