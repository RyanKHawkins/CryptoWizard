# polybius square
# Updated:  20190925

alphabet = 'abcdefghijklmnopqrstuvwxyz'

string = input("Enter message:\n")
for char in string:
    if char in ["a", "b", "c", "d"]:
        string = string.replace(char, str(alphabet.index(char) + 11))
print(string)