import re
from ngrams import ngram_score
fitness = ngram_score('quadgrams.txt')
from pycipher import Affine
'''
	Affine cipher consists of 2 keys, considered as a and b
	cipher = ap + b(mod m) 1<=a<=m , 1<=b<=m
	decrypt = a^-1(c-b)(mod m)
	
	Note:
	a should be chosen to be relatively prime to m
	a^-1 is the multiplicative inverse of a in the group of integers modulo m
	ax = 1 (mod m) here x is a^-1
'''
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
