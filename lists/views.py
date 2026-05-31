from django.shortcuts import render
from django.http import HttpResponse
from django.templatetags.static import static
import requests
file=requests.get("https://raw.githubusercontent.com/st13g/files/master/xmonad.hs")

def posts(request):
    return render(request,'lists/posts.html', {
        "title": "Posts About Everything",
        "content":"Get the latest information, insights, and news about everything that interest me",
        "img":static('images/articles.png'),
    })

def review(request):
    return render(request,'lists/reviews.html', {
        "title": "Reviews From Books",
        "content": "Some insights about every book I red",
        "img":static('images/reviews.png'),
    })

def files(request):
    return render(request,'lists/main.html', {
        "title": "This is the files",
        "img":"https://devblogs.microsoft.com/azuregov/wp-content/uploads/sites/43/2019/03/BANNER-AZ-Govt-1920x320.jpg",
    })
def linux(request):
    return render(request,'lists/linux.html', {
        "title": "Everything About Linux",
        "content":"Latest information, insights, and news about the Linux World",
        "img":static('images/linux.png'),
    })

def wiki(request):
    return render(request,'lists/wiki.html', {
        "title": "Learn With Me",
        "content": "Learn about networking, security, linux administration, cloud and language learning",
        "img":static('images/wiki.png'),
    })

def tbr(request):
    return render(request,'lists/books.html', {
        "title": "To Be Read",
        "img":static('images/tbr.jpg'),
        "content":"Some books that I'm planning to read in the nearly time",
    })

def aboutMe(request):
    return render(request,'lists/main.html', {"title": "about me",})
def files(request):
    return render(request,'lists/files.html')
