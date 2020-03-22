import re
from ngrams import ngram_score
fitness = ngram_score('quadgrams.txt')
from pycipher import Caesar

def analysis_caser(ctext):
    #All spacing/punc removed and is uppercase
    ctext = re.sub('[^A-Z]','',ctext.upper())

    #try all possible key, to find the key by using the highest fitness
    scores = []
    for i in range(26):
        scores.append((fitness.score(Caesar(i).decipher(ctext)), i))
    return max(scores)

# example ciphertext
ctext = 'YMJHFJXFWHNUMJWNXTSJTKYMJJFWQNJXYPSTBSFSIXNRUQJXYHNUMJWX'
max_key = analysis_caser(ctext) # return the tuple of values (fitness_score, key)

print 'best candidate with key (a,b) = '+str(max_key[1])+':'
print Caesar(max_key[1]).decipher(ctext)
