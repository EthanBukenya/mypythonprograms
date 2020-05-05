
# Translates letters to a corresponding encryption message
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "a":
            if letter.isupper():
             translation = translation + "Q"
            else:
                translation = translation + "q"
        elif letter.lower() in "e":
            if letter.isupper():
                translation = translation + "D"
            else:
                translation = translation + "d"
        elif letter.lower() in "i":
            if letter.isupper():
                translation = translation + "K"
            else:
                translation = translation + "k"
        elif letter.lower() in "o":
            if letter.isupper():
                translation = translation + "L"
            else:
                translation = translation + "l"
        elif letter.lower() in "u":
            if letter.isupper():
                translation = translation + "J"
            else:
                translation = translation + "j"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a word")))
