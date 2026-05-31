from django.shortcuts import render

def index(request):
    return render(request,'opinion.html')
def zephyr(request):
    return render(request,'zephyr.html')
def pinyin(request):
    return render(request,'pinyin.html')
def butterfly(request):
    return render(request,'butterfly-garden.html')
def wireshark(request):
    return render(request,'practical-packet-analysis.html')
def homeBeforeDark(request):
    return render(request,'before-dark.html')
def quassel(request):
    return render(request,'quassel.html')
def dsp(request):
    return render(request,'dsp.html')
# Create your views here.
