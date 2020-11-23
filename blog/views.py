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
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

def process_content(ARTICLE_TEXT):

    s = sys.stdout

    sentence_tokens = sent_tokenize(ARTICLE_TEXT)
    word_tokens = word_tokenize(ARTICLE_TEXT)

    try:
        tagged = nltk.pos_tag(word_tokens)

        sensationalism_score = 0

        for i in range(len(tagged)):
            if tagged[i][1] == 'JJ':
                print(tagged[i], end=" ")
                sensationalism_score += 1
            elif tagged[i][1] == 'RB':
                print(tagged[i], end=" ")
                sensationalism_score += 1
            elif tagged[i][1] == 'MD':
                print(tagged[i], end=" ")
                sensationalism_score += 1
            elif tagged[i][1] == 'PRP' or tagged[i][1] == 'PRP$':
                print(tagged[i], end=" ")
                sensationalism_score += 1
            else:
                print(tagged[i][0], end=" ")

            if i != len(tagged)-1:
                if tagged[i][0] == '.' and tagged[i+1][0] != '"':
                    print()

        print()

        print("Sensationalism Score:", end=" ")
        print(sensationalism_score/(len(tagged)))

        grammar = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""
        cp = nltk.RegexpParser(grammar)
        results = cp.parse(tagged)

        # print(tagged)
        # results.draw()
        # print(results)

        # for result in results:
        #     print(result, end=" ")

        print("Chunking Examples: ", end = " ")

        for result in results:
            if type(result) == nltk.tree.Tree:
                assoc=[]
                for res in result:
                    assoc.append(res[0])
                if len(assoc) > 2:
                    print(assoc, end=" ")

    except Exception as e:
        print(str(e))

    return s