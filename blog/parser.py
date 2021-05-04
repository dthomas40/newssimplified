import os
import sys
import nltk
# nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import sent_tokenize, word_tokenize

class ProcessManager():
    def process_article(article):

        tagged = nltk.pos_tag(word_tokenize(article))
        output = ""
        sensationalism_score = 0
        

        for i in range(len(tagged)):
            if tagged[i][1] == 'JJ':
                # output += "(" + ''.join(tagged[i][1]) + ", " + ''.join(tagged[i][0]) + ") "
                output += ''.join(tagged[i][0]) + " "
                sensationalism_score += 1
            elif tagged[i][1] == 'RB':
                # output += "(" + ''.join(tagged[i][1]) + ", " + ''.join(tagged[i][0]) + ") "
                output += ''.join(tagged[i][0]) + " "
                sensationalism_score += 1
            elif tagged[i][1] == 'MD':
                # output += "(" + ''.join(tagged[i][1]) + ", " + ''.join(tagged[i][0]) + ") "
                output += ''.join(tagged[i][0]) + " "
                sensationalism_score += 1
            elif tagged[i][1] == 'PRP' or tagged[i][1] == 'PRP$':
                # output += "(" + ''.join(tagged[i][1]) + ", " + ''.join(tagged[i][0]) + ") "
                output += ''.join(tagged[i][0]) + " "
                sensationalism_score += 1
            else:
                output += ''.join(tagged[i][0]) + " "

        output += "\nSensationalism Score:" + " "
        
        if(len(tagged) != 0):
            output += str(sensationalism_score/(len(tagged)))
        else:
            output += "NULL"

        output += "\nImportant Terms:" + " "

        grammar = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""
        cp = nltk.RegexpParser(grammar)
        results = cp.parse(tagged)
        
        for result in results:
            if type(result) == nltk.tree.Tree:
                assoc=[]
                for res in result:
                    assoc.append(res[0]+" ")
                if len(assoc) > 2:
                    output += ''.join(assoc) + ", "

        return output + "\n\n"
