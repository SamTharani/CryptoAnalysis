"# CryptoAnalysis" 

In all these crypto analysis program we have used
"Quadgram statistics"

How to calculate the fitness score?
Calculte the statistics of the deciphered text, and compare thes statistics to those calculated from standared english text
(available in quadgram.txt). A fitness function will give us a number, the higher the number the more likely the particular key

Quadgram statistics
It is also known as tetragraphs or group of 4 letters
Eg: SYSTEM -> SYST,YSTE and STEM

The probability of a specific quadgram is calculated by diciding the count of that quadgram by the total number of quadgrams in our corpus
Eg: P(SYST) = count(SYST)/N  in here N:total number of quadgrams

To compute the probability of a piece of text being English, we must extract all the quadgrams, then multiply each of the quadgram probabilities
Eg: P(SYSTEM) = P(SYST) * P(YSTE) * P(STEM)

Log probability implies
log(P(SYSTEM)) = log(P(SYST)) + log(P(YSTE)) + log(P(STEM))

higher number means it is more highly to be English

*ngrams.py and quadgram.txt are downloaded from the internet
