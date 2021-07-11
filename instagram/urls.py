from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
  path('', views.index, name='home'),
  path('account/profile', views.profile, name='uprofile'),
  path('postpic', views.post_pic, name='postpic'),
  path('userprofile/<int:id>/', views.userprofile, name='userprofile'),
  path('search/', views.searchUser, name='search_results'),
  path('imagedetails/<int:id>', views.imagedetails, name='imagedetails')
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
  