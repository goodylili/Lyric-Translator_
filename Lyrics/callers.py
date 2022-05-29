import lyricsgenius
import os
from dotenv import load_dotenv


def the_genius():
    load_dotenv()
    genius = lyricsgenius.Genius(os.getenv('KEY'))
    return genius


def get_songs_by():
    genius_caller = the_genius()
    name = input("Enter the artistes name::")
    request = input("Do you also want the features too?, y or n::")
    print(f"Here's a list of songs by {name}")
    if request.lower() == "y":
        artist = genius_caller.search_artist(f"{name}", max_songs=25, sort="title", include_features=True)
    else:
        artist = genius_caller.search_artist(f"{name}", max_songs=20, sort="title")
    return artist


def get_lyrics():
    contact_genius = the_genius()
    name = input("Enter the artistes name::")
    song_name = input("What's the song name::")
    try:
        lyrics = contact_genius.search_song(f"{song_name}", name).lyrics
    except:
        print("Either not found or no internet connection.")
        exit()
    splitter = [lyrics[i:i + 499] for i in range(0, len(lyrics), 499)]
    return splitter
