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


# Create your views here.
