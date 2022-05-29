from translate import Translator


def translater(loop_containing_lyrics):
    translated = ""
    print("You can translate to any of the languages on ISO-639-I")
    print(
        "https://en.wikipedia.org/wiki/ISO_639-1, check this out and input the 2 alpha language code to translate "
        "lyrics")
    reqqie = input("In what language do you need these lyrics!").lower()
    if len(reqqie) > 2 or reqqie.isalpha() == False:
        print("Incorrect code input, should be two letters")
        exit()
    else:

        translator = Translator(to_lang=reqqie)
        for text in loop_containing_lyrics:
            translation = translator.translate(f"{text}")
            translated += translation

    return translated
