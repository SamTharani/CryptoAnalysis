import re
from ngrams import ngram_score
fitness = ngram_score('quadgrams.txt')
from pycipher import Affine

def analysis_affine(ctext):
    #Remove spacing and non-alpha numeric characters
    ctext = re.sub('[^A-Z]','',ctext.upper())

    #to find possible keys
    scores = []
    a = [1,3,5,7,9,11,15,17,19,21,23,25]
    for i in a:
        for j in range(0,25):
            scores.extend([(fitness.score(Affine(i,j).decipher(ctext)),(i,j))])
    return max(scores)

ctext = 'YMJHFJXFWHNUMJWNXTSJTKYMJJFWQNJXYPSTBSFSIXNRUQJXYHNUMJWX'
max_key = analysis_affine(ctext)

plaintext = Affine(a=max_key[1][0],b=max_key[1][1]).decipher(ctext)
print plaintext
