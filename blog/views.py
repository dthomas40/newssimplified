from django.shortcuts import render

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


def home(request):
    context = {
        'posts': posts
    }
    print(request.POST)
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})