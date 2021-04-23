from django.http import HttpResponseRedirect
from django.shortcuts import render
from subprocess import run, PIPE
import sys
from .models import Post
from . import parser
from . import similaritycheck
from . import output
from . import automate
# Create your views here.

def button(request):
    (input1,input2) = automate.Scraper.scrape()

    process1 = parser.ProcessManager.process_article(input1)
    process2 = parser.ProcessManager.process_article(input2)
    process3 = similaritycheck.ComparisonManager.compare_articles(input1,input2)

    parser_out = output.Formatter.format(process1, process2, process3)

    title = "Automation Debugging: Newer Test Run"
    genre = "World"
    author1 = "Unknown"
    author2 = "Unknown"
    url1 = "www.google.com"
    url2 = "www.google.com"

    Post.objects.create_post(title, parser_out, genre[0].capitalize(), author1, author2, url1, url2)

    context = {
        'posts': Post.objects.all()
    }

    return render(request, 'blog/home.html', context)

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

    process1 = parser.ProcessManager.process_article(input1)
    process2 = parser.ProcessManager.process_article(input2)
    process3 = similaritycheck.ComparisonManager.compare_articles(input1,input2)

    parser_out = output.Formatter.format(process1, process2, process3)

    context = {
        'posts': Post.objects.all(),
        # 'data2': parser_out
    }

    Post.objects.create_post(title, parser_out, genre[0].capitalize(), "Unknown", "Unknown", "www.google.com", "www.google.com")

    return render(request,'blog/home.html',context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})