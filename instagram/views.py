from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Profile, Location, Comments
from .form import UserForm, ProfileForm, PostPicForm, CommentForm
from django.contrib import messages

@login_required(login_url='accounts/login')
def index(request):
  if request.method == 'POST':
    commentForm = CommentForm(request.POST)
    if commentForm.is_valid():
      pic_id = int(request.POST.get('imageid'))
      pic = Post.objects.get(id=pic_id)
      com = commentForm.save(commit=False)
      com.user = request.user
      com.pic = pic
      com.save()
    return redirect('/#image'+str(pic_id))
  
  title = 'this is title'
  allpics = Post.all_pictures()
  commentForm = CommentForm()
  allcomments = Comments.objects.all()
  print(allcomments)
  return render(request, 'index.html', {'title': title, 'allpics':allpics, 'commentForm':commentForm, 'allcomments':allcomments})

@login_required(login_url='accounts/login')
def profile(request):

  if request.method == 'POST':
    user_form = UserForm(request.POST, instance=request.user)
    profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)

    if user_form.is_valid() and profile_form.is_valid():
      user_form.save()
      profile_form.save()
      messages.success(request,('Your profile was successfully updated!'))
    return redirect('uprofile')

  title = 'Profile'
  user_form = UserForm(instance=request.user)
  profile_form = ProfileForm(instance=request.user)

  user_pics = Post.user_pictures(request.user.username)
  return render(request, 'profile/index.html', {'title':title, "user":request.user, "user_form":user_form, 'profile_form':profile_form, 'user_pics':user_pics})

# Create your views here.
