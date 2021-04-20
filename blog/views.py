from django.http import HttpResponseRedirect
from django.shortcuts import render
from subprocess import run, PIPE
import sys
from .models import Post
from . import parser
from . import similaritycheck
from . import output
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
    page = requests.get('https://news.google.com/topstories?hl=en-US&gl=US&ceid=US%3Aen')
    bSoup = BeautifulSoup(page.content, 'html.parser')
    links_list = bSoup.find_all('a')
    links = []
    for link in links_list:
        if 'href' in link.attrs:
            links.append(str(link.attrs['href']) + '\n')

    i = 0
    art1_url = links[i]
    while art1_url[:10] != './articles':
        art1_url = links[i]
        i += 1

    art2_url = art1_url

    while art1_url == art2_url or './publications' in art2_url or './topics' in art2_url or './stories' in art2_url:
        art2_url = links[i]
        i += 1

    art1_url = 'https://news.google.com/' + art1_url[2:]
    art2_url = 'https://news.google.com/' + art2_url[2:]

    article1 = Article(art1_url)
    article2 = Article(art2_url)
    article1.download()
    article1.parse()
    article1.nlp()
    article2.download()
    article2.parse()
    article2.nlp()


    genre = request.POST.get('genre')
    title = request.POST.get('title')
    input1 = article1
    input2 = article2

    process1 = parser.ProcessManager.process_article(input1)
    process2 = parser.ProcessManager.process_article(input2)
    process3 = similaritycheck.ComparisonManager.compare_articles(input1,input2)

    parser_out = output.Formatter.format(process1, process2, process3)

    context = {
        'posts': Post.objects.all(),
        'data2': parser_out
    }

    Post.objects.create_post(title, parser_out, genre[0].capitalize())

    return render(request,'blog/home.html',context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})