# Name:  string_formatting.py
# Updated:  20191004

alphabet = 'abcdefghijklmnopqrstuvwxyz'


# remove all punctiation and spaces

def strip_string(string):
    for char in string:
        if char not in alphabet:
            string = string.replace(char, "")
    return string

    # return (char for char in string if char in alphabet)

# group characters into equal parts
def group_characters(string, num=3, null='x'):
    grouped_string = ""

    i = len(string)
    j = 0
    while j < i:
        for k in range(num):
            if j < i:
                grouped_string += string[j]
                j += 1
            else:
                grouped_string += null
        grouped_string += " "
    return grouped_string
