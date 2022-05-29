import lyricsgenius
import os
from dotenv import load_dotenv


def the_genius():
    load_dotenv()
    genius = lyricsgenius.Genius(os.getenv('KEY'))
    return genius


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
