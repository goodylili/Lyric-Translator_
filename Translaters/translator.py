from googletrans import Translator

def translate(list_containing_lyrics):
    translator = Translator()
    translated = ""
    print("You can translate to any of the languages on ISO-639-I")
    print(
        "https://en.wikipedia.org/wiki/ISO_639-1, check this out and input the 2 alpha language code to translate "
        "lyrics")
    user_request = input("In what language do you need these lyrics!").lower()
    if len(user_request) > 2 or user_request.isalpha() == False:
        print("Incorrect code input, should be two letters and a ISO 631 language code")
        exit()
    else:
        for text in list_containing_lyrics:
            translated_text = translator.translate(f"{text}", dest=f"{user_request}")
            translated += str(translated_text)

    return translated
