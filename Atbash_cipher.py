from pycipher import Atbash

def encrypt(plaintext):
    return Atbash().encipher(plaintext)

def decrypt(ciphertext):
    return Atbash().decipher(ciphertext)


#Examples
encrypt('defend the east wall of the castle')
decrypt('wvuvmwgsvvzhgdzoolugsvxzhgov')

from pycipher import Rot13

def encrypt(plaintext):
    return Rot13().encipher(plaintext)

def decrypt(ciphertext):
    return Rot13().decipher(ciphertext)
