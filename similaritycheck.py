import sys
import nltk
nltk.download('all-corpora')
from nltk import sent_tokenize, word_tokenize, pos_tag
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import wordnet as wn
import time
start_time = time.time()

article1 = ("%s" %(sys.argv[1]))
article2 = ("%s" %(sys.argv[2]))

def small_tag(tag):
    if tag.startswith('N'):
        return 'n'
    if tag.startswith('V'):
        return 'v'
    if tag.startswith('J'):
        return 'a'
    if tag.startswith('R'):
        return 'r'
    if tag.startswith('W'):
        return 'w'
    if tag.startswith('E'):
        return 'e'
    if tag.startswith('E'):
        return 'p'
    return None

if __name__ == '__main__':
    art1 = []
    art2 = []
    # Split articles up by sentences
    art1words = []
    art2words = []
    similarities = []
    #with open('article1.txt', encoding="utf8") as f:
    sentences = sent_tokenize(article1)
    for i in sentences:
        art1.append(i)
    #with open('article2.txt', encoding="utf8") as f:
    sentences = sent_tokenize(article2)
    for i in sentences:
        art2.append(i)

    # Tokenize each sentence with their pos_tag
    match_tokenizer = RegexpTokenizer("[\w']+")
    i = 0
    while i < (len(art1)):
        if len(match_tokenizer.tokenize(art1[i])) < 5 or \
                pos_tag(match_tokenizer.tokenize(art1[i]))[0][1] == 'CC':
            art1[(i-1):(i+1)] = [''.join(art1[(i-1):(i+1)])]
            i -= 1
        i += 1

    while i < (len(art2)):
        if len(match_tokenizer.tokenize(art2[i])) <= 5 or \
                pos_tag(match_tokenizer.tokenize(art2[i]))[0][1] == 'CC':
            art2[(i-1):(i+1)] = [''.join(art2[(i-1):(i + 1)])]
            i -= 1
        i += 1

    for i in art1:
        art1words.append(pos_tag(match_tokenizer.tokenize(i)))
    for i in art2:
        art2words.append(pos_tag(match_tokenizer.tokenize(i)))
    a1count = 0

    for i in art1words:
        a2count = 0
        syns = []
        for j in i:
            tag = j[1]
            wn_tag = small_tag(tag)
            try:
                w = wn.synsets(j[0], wn_tag)[0]
            except:
                w = None
            if w is not None:
                syns.append(w)
        for k in art2words:
            #print(i, "|||||||", k)
            syns2 = []
            for l in k:
                tag = l[1]
                wn_tag = small_tag(tag)
                try:
                    w = wn.synsets(l[0], wn_tag)[0]
                except:
                    w = None
                if w is not None:
                    syns2.append(w)
            score, count = 0.0, 0
            for s in syns:
                best_score = ([s.path_similarity(ss) for ss in syns2])
                res = [i for i in best_score if i]

                if res:
                    x = max(res)
                    if x is not None:
                        score += x
                        count += 1
                    score /= count
            sentence_similarity = (score, art1[a1count], art2[a2count])
            similarities.append(sentence_similarity)
            a2count += 1
        a1count += 1

    similarities.sort(reverse=True)
    #with open('result_file.txt', 'w') as f:
    #    f.write("\n".join(str(item) for item in similarities))
    for i in similarities:
        print(i)
    print("--- %s seconds ---" % (time.time() - start_time))