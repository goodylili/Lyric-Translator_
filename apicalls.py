import lyricsgenius


def the_genius():
    api_key = "Your API key here"
    genius = lyricsgenius.Genius(api_key)
    return genius

def get_songsby():
    genius_caller = the_genius()
    n_ame = input("Enter the artistes name::")
    reques = input("Do you also want the features too?, y or n::")
    print(f"Here's a list of songs by {n_ame}")
    if reques.lower() == "y":
        artist = genius_caller.search_artist(f"{n_ame}", max_songs=25, sort="title", include_features=True)
    else:
        artist = genius_caller.search_artist(f"{n_ame}", max_songs=20, sort="title")
    return artist




def get_lyrics():
    contact_genius = the_genius()
    n_ame = input("Enter the artistes name::")
    song_name = input("What's the song name::")
    try:
        lyrice = contact_genius.search_song(f"{song_name}", n_ame).lyrics
    except:
        print("Either not found or no internet connection.")
        exit()
    splitter = [lyrice[i:i + 499] for i in range(0, len(lyrice), 499)]
    return splitter


