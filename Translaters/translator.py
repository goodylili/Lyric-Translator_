from translate import Translator


def translater(loop_containing_lyrics):
    translated = ""
    print("You can translate to any of the languages on ISO-639-I")
    print(
        "https://en.wikipedia.org/wiki/ISO_639-1, check this out and input the 2 alpha language code to translate "
        "lyrics")
    user_request = input("In what language do you need these lyrics!").lower()
    if len(user_request) > 2 or user_request.isalpha() == False:
        print("Incorrect code input, should be two letters")
        exit()
    else:
        translator = Translator(to_lang=user_request)
        for text in loop_containing_lyrics:
            translation = translator.translate(f"{text}")
            translated += translation

    return translated
