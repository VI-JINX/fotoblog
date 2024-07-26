from django import forms
from . models import *
from django.contrib.auth import get_user_model

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('image', 'captions')

class BlogForm(forms.ModelForm):
    edit_blog = forms.BooleanField(widget=forms.HiddenInput, initial = True)
    
    class Meta:
        model = Blog
        fields = ['title', 'content']

class DeleteBlogForm(forms.Form):
    delete_blog = forms.BooleanField(widget=forms.HiddenInput, initial = True)




