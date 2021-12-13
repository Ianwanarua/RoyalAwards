from awwards.models import Profile, Project, Rates
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    full_name = forms.CharField(max_length=50, required=False)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user', 'profile', 'date']


class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Required.')

    class Meta:
        model = User
        fields = ('username', 'email')


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        # fields = ['bio','profile_pic']
        fields = ['contact', 'profile_pic', 'bio']


class RatingsForm(forms.ModelForm):
    class Meta:
        model = Rates
        fields = ['design', 'creativity', 'usability', 'content']
        # exclude = ['user','project','average']
