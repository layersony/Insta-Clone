from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Profile, Location, Comments, Follow
from .form import UserForm, ProfileForm, PostPicForm, CommentForm, LikeForm
from django.contrib import messages
from django.http import Http404, HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import User
from .email import send_welcome_email

@login_required(login_url='accounts/login')
def index(request):
  if request.method == 'POST':
    commentForm = CommentForm(request.POST)
    likeform = LikeForm(request.POST)
    if commentForm.is_valid():
      pic_id = int(request.POST.get('imageid'))
      pic = Post.objects.get(id=pic_id)
      com = commentForm.save(commit=False)
      com.user = request.user
      com.pic = pic
      com.save()
    
    # if likeform.is_valid():
    #   like_id = int(request.POST.get('imageid'))
    #   likes = Post.objects.get(id=like_id)
    #   like = commentForm.save(commit=False)
    #   like.user = request.user
    #   like.pic = likes
    #   like.save()

    return redirect('/#image'+str(pic_id))

  if request.method == 'GET' and Profile.objects.get(username = request.user).count  == 0:
    user_email = User.objects.get(username = request.user).email
    send_welcome_email(request.user, user_email)
    Profile.objects.filter(username = request.user).update(count = 1)

  title = 'this is title'
  allpics = Post.all_pictures()
  commentForm = CommentForm()
  likeform = LikeForm()
  allcomments = Comments.objects.all()
  return render(request, 'index.html', {'title': title, 'allpics':allpics, 'commentForm':commentForm, 'allcomments':allcomments, 'likeform':likeform})

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

@login_required(login_url='accounts/login')
def post_pic(request):
  if request.method == 'POST':
    postForm = PostPicForm(request.POST, request.FILES)
    if postForm.is_valid():
      pic = postForm.save(commit=False)
      pic.uploadedBy = request.user
      pic.save()
      messages.success(request, 'Image Uploaded successfully')
    return redirect('uprofile')

  postForm = PostPicForm()
  return render(request, 'profile/postpic.html', {'postForm':postForm, 'user':request.user})

def userprofile(request, id):
  try:
    user = Profile.objects.get(id = id)
    user_pics = Post.user_pictures(user.username)
    followers = User.objects.get(username = request.user.username).follower.all()
    
    foll_list = [follower.following.id for follower in followers]
    if request.user.id in foll_list:
      is_following = True
    else:
      is_following = False
    if request.user.username == str(user.username):
      return redirect('uprofile')
    else:
      using_user = User.objects.get(username = user.username)
      return render(request, 'userprofile.html', {'using_user': using_user,'userprofile':user, 'user_pics':user_pics, "is_following": is_following})
  except Profile.DoesNotExist:
    return HttpResponseRedirect(', Sorry the Page You Looking For Doesnt Exist.')

def searchUser(request):
  if 'search' in request.GET and request.GET['search']:
    search_term = request.GET.get('search')
    searchprofiles = Profile.searchProfile(search_term)
    return render(request, 'search.html', {'searchresults':searchprofiles})
  else:
    return redirect('home')

def imagedetails(request, id):
  if request.method == 'POST':
    commentForm = CommentForm(request.POST)
    if commentForm.is_valid():
      pic_id = int(request.POST.get('imageid'))
      pic = Post.objects.get(id=pic_id)
      com = commentForm.save(commit=False)
      com.user = request.user
      com.pic = pic
      com.save()
    return redirect('imagedetails', id=id)

  commentForm = CommentForm(request.POST)
  pic = Post.objects.get(id = id)
  allcomments = Comments.objects.all()
  return render(request, 'imagedetails.html', {'specificpic':pic, 'commentForm':commentForm, 'allcomments':allcomments})

def followuserpro(request):
  user = User.objects.get(id = request.POST.get("id"))
  followed = None

  if Follow.objects.filter(follower = user, following = request.user):
      Follow.objects.filter(follower = user, following = request.user).delete()
      followed = 0
      count = user.follower.all().count()
  else:
      Follow.objects.create(follower = user, following = request.user)
      followed = 1
      count = user.follower.all().count()
  data = {"hey":"hey", "followed":followed, "count":count}
  return JsonResponse(data)
