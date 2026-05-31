from django.urls import path,include
from . import views

urlpatterns = [
    path('posts/',views.posts,name='lists'),
    path('review/',views.review,name='lists'),
    path('files/',views.files,name='lists'),
    path('linux/',views.linux,name='lists'),
    path('wiki/',views.wiki,name='lists'),
    path('tbr/',views.tbr,name='lists'),
    path('aboutMe/',views.aboutMe,name='lists'),
    path('files/',views.files,name='lists'),
    path('',include('content.urls')),
]
