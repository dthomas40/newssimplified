from django.http import HttpResponseRedirect
from django.shortcuts import render
from subprocess import run, PIPE
import sys
# Create your views here.

posts = [
    {
        'author': 'Alan Paul',
        'title': 'Article 1',
        'content': 'First post content',
        'date_posted': 'October 25, 2020'
    },
    {
        'author': 'Anna Paul',
        'title': 'Article 2',
        'content': 'Second post content',
        'date_posted': 'October 26, 2020'
    },
    {
        'author': 'Don Thomas',
        'title': 'Article 3',
        'content': 'Third post content',
        'date_posted': 'October 27, 2020'
    },
    {
        'author': 'Alwin Tomy',
        'title': 'Article 4',
        'content': 'Fourth post content',
        'date_posted': 'October 28, 2020'
    },
    {
        'author': 'Joel Binu George',
        'title': 'Article 5',
        'content': 'Fifth post content',
        'date_posted': 'October 29, 2020'
    },
    {
        'author': 'Ankitha Sreekumar',
        'title': 'Article 6',
        'content': 'Sixth post content',
        'date_posted': 'October 30, 2020'
    }
]
def button(request):
    return render(request, 'home.html')

def home(request):
    import requests
    data = requests.get("https://www.google.com")
    print(data.text)
    data=data.text
    context = {
        'posts': posts
    }
    print(request.POST)
    return render(request, 'blog/home.html', context)

def external(request):
    input1 = request.POST.get('article1')
    input2 = request.POST.get('article2')
    out = run([sys.executable,'similaritycheck.py', input1,input2], shell=False, stdout=PIPE)
    print(out)

    return render(request,'blog/home.html',{'data1':out.stdout})

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})