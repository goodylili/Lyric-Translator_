from Translathor import translator
from apicalls import *

def caller():
    intention = input(
        "To get songs by an artist use (F)\nTo get music lyrics use(G)\nUse (H) to get lyrics and translate -->")
    if intention.lower() not in ['f', 'g', 'h'] :
        exit("Lmao, get serious abeg")
    elif intention.lower() == "g":
        for text in get_lyrics():
            print(text)

    elif intention.lower() == "f":
        get_songsby()

    else:
        print(translator(get_lyrics()))

if __name__ == "__main__":
    print(caller())
