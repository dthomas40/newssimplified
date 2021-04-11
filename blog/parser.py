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


def process_content(article):
    processed = ""   
    sentence_tokens = sent_tokenize(article)
    word_tokens = word_tokenize(article)

    try:
        tagged = nltk.pos_tag(word_tokens)

        sensationalism_score = 0

        for i in range(len(tagged)):
            if tagged[i][1] == 'JJ':
                print(tagged[i], end=" ")
                processed += tagged[i] + " "
                sensationalism_score += 1
            elif tagged[i][1] == 'RB':
                print(tagged[i], end=" ")
                processed += tagged[i] + " "
                sensationalism_score += 1
            elif tagged[i][1] == 'MD':
                print(tagged[i], end=" ")
                processed += tagged[i] + " "
                sensationalism_score += 1
            elif tagged[i][1] == 'PRP' or tagged[i][1] == 'PRP$':
                print(tagged[i], end=" ")
                processed += tagged[i] + " "
                sensationalism_score += 1
            else:
                print(tagged[i][0], end=" ")
                processed += tagged[i][0] + " "

            if i != len(tagged)-1:
                if tagged[i][0] == '.' and tagged[i+1][0] != '"':
                    print()
                    processed += "\n"

        print()
        processed += "\n"

        print("Sensationalism Score:", end=" ")
        processed += "Sensationalism Score:" + " "
        print(sensationalism_score/(len(tagged)))
        processed += sensationalism_score/(len(tagged))

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
                    processed += assoc

    except Exception as e:
        print(str(e))
        processed += str(e)
    
    return processed

class ProcessManager():
    def process_article(article1, article2):

        article = article1 + "\n" + "\n" + article2
        tagged = nltk.pos_tag(word_tokenize(article))
        output = ""
        sensationalism_score = 0
        

        for i in range(len(tagged)):
            if tagged[i][1] == 'JJ':
                output += "{" + ''.join(tagged[i][0]) + ", " + ''.join(tagged[i][0]) + "} "
                sensationalism_score += 1
            elif tagged[i][1] == 'RB':
                output += "{" + ''.join(tagged[i][0]) + ", " + ''.join(tagged[i][0]) + "} "
                sensationalism_score += 1
            elif tagged[i][1] == 'MD':
                output += "{" + ''.join(tagged[i][0]) + ", " + ''.join(tagged[i][0]) + "} "
                sensationalism_score += 1
            elif tagged[i][1] == 'PRP' or tagged[i][1] == 'PRP$':
                output += "{" + ''.join(tagged[i][0]) + ", " + ''.join(tagged[i][0]) + "} "
                sensationalism_score += 1
            else:
                output += ''.join(tagged[i][0]) + " "

        return output
