'''
It is a type of substitution Cipher in which each letter in the plaintext is shiffted a
certain number of places down the alphabet
e(x) = (x+k)%26
x = character in the plain text
k = key or number of shifts

d(x) = (x-k)%26
'''

#Map letters with numbers
lett_2_num = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",range(26)))
num_2_let = dict(zip(range(26),"ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

key = 3
text = "encrypt me if you can! try and catchup "

#Encryption
ciphertext = ""

for t in text.upper():
    if t.isalpha(): ciphertext += num_2_let[ (lett_2_num[t] + key)%26 ]
    else: ciphertext += t

plaintext = ""
#Decryption
for t in ciphertext.upper():
    if t.isalpha(): plaintext += num_2_let[ (lett_2_num[t] - key)%26 ]
    else: plaintext += t

print text
print ciphertext
print plaintext
