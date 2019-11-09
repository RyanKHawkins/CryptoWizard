"""
Keyword Reverse
kw_rev.py
Updated:  20191004
"""

import random
from keyword_shift import get_keyword

alphabet = 'abcdefghijklmnopqrstuvwxyz'


def set_keyword_reverse(keyword):
    # keyword = input("Keyword:  ").lower()

    new_abc = ""
    for char in keyword:
        if char in alphabet:
            if not char in new_abc:
                new_abc += char
    for letter in alphabet[::-1]:
        if not letter in new_abc:
            new_abc += letter
    return new_abc
