from django.urls import path
from django.http import HttpResponse
from . import views

urlpatterns =[
    path('this-is/',views.index,name='lists'),
    path('pinyin/',views.pinyin,name='lists'),
    path('zephyr/',views.zephyr,name='lists'),
    path('butterfly-garden/',views.butterfly,name='lists'),
    path('wireshark/',views.wireshark,name='lists'),
    path('home-before-dark/',views.homeBeforeDark,name='lists'),
    path('quassel/',views.quassel,name='lists'),
    path('signal-processing/',views.dsp,name='lists'),
]
