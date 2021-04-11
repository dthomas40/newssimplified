import os
import sys

import nltk
# nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import sent_tokenize, word_tokenize

# with open(os.path.join(sys.path[0], "article.txt"), "r") as f:
#     ARTICLE_TEXT = f.read()
# f.close()

# print(ARTICLE_TEXT)

# sentence_tokens = sent_tokenize(ARTICLE_TEXT)
# word_tokens = word_tokenize(ARTICLE_TEXT)


def process_content():
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


# sys.stdout = open("results.txt", "w")
# process_content()
# raise SystemExit(0)
# sys.stdout.close()

class ProcessManager():
    def process_article(article):
        sentence_tokens = sent_tokenize(article)
        word_tokens = word_tokenize(article)
        sys.stdout = open("results.txt", "w")
        process_content()

        with open(os.path.join(sys.path[0], "results.txt"), "r") as f:
            output = f.read()
        f.close()

        return output
