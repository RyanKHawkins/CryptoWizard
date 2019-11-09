# Name:  number_sub.py
# Updated:  20191008

alphabet = 'abcdefghijklmnopqrstuvwxyz'


def encrypt_number_sub(plaintext):
    ciphertext = plaintext

    ciphertext = ciphertext.replace("a", "01")
    ciphertext = ciphertext.replace("b", "02")
    ciphertext = ciphertext.replace("c", "03")
    ciphertext = ciphertext.replace("d", "04")
    ciphertext = ciphertext.replace("e", "05")
    ciphertext = ciphertext.replace("f", "06")
    ciphertext = ciphertext.replace("g", "07")
    ciphertext = ciphertext.replace("h", "08")
    ciphertext = ciphertext.replace("i", "09")
    ciphertext = ciphertext.replace("j", "10")
    ciphertext = ciphertext.replace("k", "11")
    ciphertext = ciphertext.replace("l", "12")
    ciphertext = ciphertext.replace("m", "13")
    ciphertext = ciphertext.replace("n", "14")
    ciphertext = ciphertext.replace("o", "15")
    ciphertext = ciphertext.replace("p", "16")
    ciphertext = ciphertext.replace("q", "17")
    ciphertext = ciphertext.replace("r", "18")
    ciphertext = ciphertext.replace("s", "19")
    ciphertext = ciphertext.replace("t", "20")
    ciphertext = ciphertext.replace("u", "21")
    ciphertext = ciphertext.replace("v", "22")
    ciphertext = ciphertext.replace("w", "23")
    ciphertext = ciphertext.replace("x", "24")
    ciphertext = ciphertext.replace("y", "25")
    ciphertext = ciphertext.replace("z", "26")

    ciphertext = "-".join(ciphertext).replace("- -", " ")

    return ciphertext