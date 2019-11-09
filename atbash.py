# Name:  atbash.py
# Updated:  20190925

alphabet = 'abcdefghijklmnopqrstuvwxyz'
reverse_alphabet = 'zyxwvutsrqponmlkjihgfedcba'


# Convert Atbash. Use for both encrypt and decrypt,
# since they're exactly the same algorithm.
def convert_atbash(plaintext):
    ciphertext = ""
    for char in plaintext:
        if char in alphabet:
            index = alphabet.index(char)
            ciphertext += reverse_alphabet[index]
        else:
            ciphertext += char
    return ciphertext


# Brief explanation of the Atbash cipher
def summarize_atbash():
    pass
