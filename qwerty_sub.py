alphabet = 'abcdefghijklmnopqrstuvwxyz'
qwerty_alphabet = 'qwertyuiopasdfghjklzxcvbnm'

def convert_qwerty(plaintext):
    ciphertext = ""
    for char in plaintext:
        if char in alphabet:
            index = alphabet.index(char)
            ciphertext += qwerty_alphabet[index]
        else:
            ciphertext += char
    return ciphertext