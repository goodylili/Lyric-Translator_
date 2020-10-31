import lyricsgenius

from translate import Translator


class Lyric_translator:
    def __init__(self, name=input("Enter Your name::")):
        self.genius = lyricsgenius.Genius("KeGxzMT4aOxBHo4dQjdBaQ5Q6n1TBA07EyRID7AJ-JQJNoj-JGS9DQ0tAYDkElKO")
        print(
            f"Welcome {name} This program uses Genius's API.\nPlease Do you mind not hitting their servers by running in series..\nI don't want to loose my developers account... Thank you.")

    def get_songsby(self):
        n_ame = input("Enter the artistes name::")
        print(f"These are the songs by {n_ame}")

        reques = input("Do you also want the features too?, y or n::")
        if reques.lower() == "y":
            artist = self.genius.search_artist(f"{n_ame}", max_songs=25, sort="title", include_features=True)
            print(artist.songs)
        else:
            artist = self.genius.search_artist(f"{n_ame}", max_songs=20, sort="title")
            print(artist.songs)

    def get_lyrics(self):
        n_ame = input("Enter the artistes name::")
        song_name = input("What's the song name::")
        try:
            lyrice = self.genius.search_song(f"{song_name}", n_ame).lyrics
        except:
            print("Either not found or no internet connection.")
            exit()
        print(
            "You can translate to English, Spanish, Portuguese and Chinese by correctly inputting the values as specified.")
        reqqie = input("In what language do you need these lyrics!")
        # Translate takes in 499 arguments so i'm having to shorten text and loop
        splitter = [lyrice[i:i + 499] for i in range(0, len(lyrice), 499)]
        if reqqie.lower() == "english":
            translator = Translator(to_lang="en")

        if reqqie.lower() == "spanish":
            translator = Translator(to_lang="es")

        if reqqie.lower() == "portuguese":
            translator = Translator(to_lang="pt")

        if reqqie.lower() == "chinese":
            translator = Translator(to_lang="zh")

        for text in splitter:
            translation = translator.translate(f"{text}")
            print(translation)


random_user = Lyric_translator()
what = input("Enter (l) to get a list of song from an artiste and (t) for lyrics and translations!")
if what.lower() == "l":
    random_user.get_songsby()
    print(random_user)
if what.lower() == "t":
    random_user.get_lyrics()
    print(random_user)
