from Translaters.translator import translater
from Lyrics.callers import *


def caller():
    intention = input(
        "To get songs by an artist use (F)\nTo get music lyrics use(G)\nUse (H) to get lyrics and translate -->")
    if intention.lower() not in ['f', 'g', 'h']:
        exit("Lmao, get serious!")
    elif intention.lower() == "g":
        for text in get_lyrics():
            print(text)

    elif intention.lower() == "f":
        get_songs_by()

    else:
        print(translater(get_lyrics()))


if __name__ == "__main__":
    print(caller())
