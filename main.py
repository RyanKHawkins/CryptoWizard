# Cryptography Program
# Updated:  20190928

import os

from atbash import convert_atbash
from reverse import reverse_cipher2
from shift_substitution import encrypt_shift_substitution, decrypt_shift_substitution, convert_rot13, encrypt_caesar, decrypt_caesar
from keyword_shift import encrypt_keyword_sub, decrypt_keyword_sub
from string_formatting import strip_string, group_characters
from morse_code import encrypt_morse_code
from number_sub import encrypt_number_sub

alphabet = 'abcdefghijklmnopqrstuvwxyz'
reverse_alphabet = 'zyxwvutsrqponmlkjihgfedcba'


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def next_screen():
    input("\n\nHit ENTER to continue.\n")
    clear()


def display_header(header):
    print(header.title())
    print('-' * len(header))


def get_message():
    message = input('Enter your message:\n').lower()
    return message


cipher_options = {
    1: 'Caesar',
    2: 'Shift Subtitution',
    3: 'Keyword Shift',
    4: 'Rot13',
    5: 'Atbash',
    6: 'Reverse',
    7: 'Morse Code',
    8: 'Number Substitution'
}


def show_cipher_options():
    print()
    display_header('Ciphers')
    for key, value in cipher_options.items():
        print(f"- {value}")


def choose_cipher():
    show_cipher_options()
    cipher_choice = input('\nChoose one:  ').lower()
    return cipher_choice


def encrypt_message():
    print("Encryption...")
    cipher_choice = choose_cipher()
    encrypted_message = ""
    if cipher_choice in ['caesar', 'ceasar', 'caeser', 'cesar']:
        encrypted_message = encrypt_caesar(get_message())
    elif cipher_choice in ['rot13']:
        encrypted_message = convert_rot13(get_message())
    elif cipher_choice in ['shift substitution', 'shift', 'sub']:
        encrypted_message = encrypt_shift_substitution(get_message())
    elif cipher_choice in ['keyword', 'kw', 'keyword shift']:
        encrypted_message = encrypt_keyword_sub(get_message())
    elif cipher_choice in ['atbash', 'atb']:
        encrypted_message = convert_atbash(get_message())
    elif cipher_choice in ['reverse', 'rev']:
        encrypted_message = reverse_cipher2(get_message())
    elif cipher_choice in ['morse', 'morse code', 'morsecode', 'mc']:
        encrypted_message = encrypt_morse_code(get_message())
    elif cipher_choice in ['number sub', 'number substitution']:
        encrypted_message = encrypt_number_sub(get_message())
    else:
        print("Invalid Option")
        next_screen()
    if encrypted_message != "":
        print(f"\nEncrypted message:  {encrypted_message}")


def decrypt_message():
    print("Decrypting...")
    cipher_choice = choose_cipher()
    print(cipher_choice.title())
    print()
    decrypted_message = ""
    if cipher_choice in ['caesar', 'ceasar', 'caeser']:
        decrypted_message = decrypt_caesar(get_message())
    elif cipher_choice in ['rot13']:
        decrypted_message = convert_rot13(get_message())
    elif cipher_choice in ['shift substitution', 'shift', 'sub']:
        decrypted_message = decrypt_shift_substitution(get_message())
    elif cipher_choice in ['keyword', 'kw', 'keyword shift']:
        print("Option Pending...")
        pass
    elif cipher_choice in ['atbash', 'atb']:
        decrypted_message = convert_atbash(get_message())
    elif cipher_choice in ['reverse', 'rev']:
        decrypted_message = reverse_cipher2(get_message())
    elif cipher_choice in ['morse', 'morse code', 'morsecode', 'mc']:
        print("Option Pending...")
        pass
    else:
        print("Invalid Option")
        next_screen()
        decrypt_message()
    if decrypted_message != "":
        print(f"\nDecrypted Message:  {decrypted_message}")


title = "C i p h e r  W i z a r d"

intro_message = """
\"This is combination of two of my hobbies 
(cryptography and programming). I hope 
you find this program fun and useful.\"
- Ryan Hawkins
"""


def main_intro():
    print()
    print(title)
    print()
    print("-" * 40)
    print(intro_message)
    print("-" * 40)


def main():

    main_intro()

    next_screen()

    keep_going = True
    while keep_going:
        display_header("Main Menu")

        print("E:  Encrypt")
        print("D:  Decrypt")
        # print("S:  Solve")
        print("Q:  Quit/Exit")
        choice = input("\nChoose one:  ")

        if choice in ["exit", "x", "ex", "q", "quit"]:
            keep_going = False
            print()
            print("Have a nice day.")
        elif choice in ['e', 'en', 'enc', 'encrypt', 'encipher', 'encode']:
            encrypt_message()
            next_screen()
        elif choice in ['d', 'de', 'dec', 'decrypt', 'decipher', 'decode']:
            decrypt_message()
            next_screen()
        else:
            pass


# if __name__ == "__main__":
#     main()

# print(f"\nThank you for using {title}.")
# print("I hope it was enjoyable and useful.")

import rand_alpha