from Translaters.translator import translate
from Lyrics.callers import *


def caller():
    intention = input(
        "To get music lyrics use(G)\nUse (H) to get lyrics and translate -->")
    if intention.lower() not in ['f', 'g', 'h']:
        exit("Seriously? like seriously?")
    elif intention.lower() == "g":
        for text in get_lyrics():
            print(text)



    else:
        print(translate(get_lyrics()))


if __name__ == "__main__":
    print(caller())
