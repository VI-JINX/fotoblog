from django import forms
from django.contrib.auth.forms import UserCreationForm
from  django.contrib.auth import get_user_model
from . models import *

class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'role')

class ProfilPhotoForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['photo_profil']

class FollowUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['follows']

