from django.http import HttpResponseRedirect
from django.shortcuts import render
from subprocess import run, PIPE
import sys
from .models import Post
from . import parser
# Create your views here.

def button(request):
    return render(request, 'home.html')

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    print(request.POST)
    return render(request, 'blog/home.html', context)

def external(request):
    genre = request.POST.get('genre')
    title = request.POST.get('title')
    input1 = request.POST.get('article1')
    input2 = request.POST.get('article2')
    out = run([sys.executable,'similaritycheck.py', input1,input2], shell=False, stdout=PIPE)
    article1_out = parser.ProcessManager.process_article(input1)
    article2_out = parser.ProcessManager.process_article(input2)
    parser_out = article1_out + "\n" + "\n" + article2_out
    print(out)

    context = {
        'posts': Post.objects.all(),
        'data1': out.stdout,
        'data2': parser_out
    }

    Post.objects.create_post(title, parser_out, genre[0].capitalize())

    return render(request,'blog/home.html',context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})