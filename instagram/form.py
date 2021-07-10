from django import forms
from django.contrib.auth.models import User
from .models import Profile, Post, Comments

class UserForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ('username', 'email')

class ProfileForm(forms.ModelForm):
  
  class Meta:
    model = Profile
    exclude = ('username',)
    fields = ('fullName', 'bio', 'profilePic', 'phoneNumber', 'gender')
  
class PostPicForm(forms.ModelForm):
  class Meta:
    model = Post
    exclude = ('uploadedBy', 'posted')
    fields = '__all__'

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comments
    exclude = ('pic', 'user')
    fields = '__all__'
    