from django.shortcuts import render
from .models import Post

# Create your views here.

# list of dictionaries

posts= [
        {
        'author': "Sanika K",
        'title': "How I start my day",
        "content": "-This is how I start my day-",
        "date_posted": "April 4th, 2021"
        },
        {
        'author': "Sanika K",
        'title': "How I end my day",
        "content": "-This is how I end my day-",
        "date_posted": "April 4th, 2021"
        },
]

def Home(request):
    #reference to the list of dictionaries
    context= {
        "posts": Post.objects.all()
    }
    return render(request, 'blog/Home.html',context)

def About(request):
    return render(request, 'blog/About.html', {"title": "This is a title"})
