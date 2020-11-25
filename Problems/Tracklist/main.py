def tracklist(**params):
    for elem in params:
        print(f"{elem}")
        for keys in params[elem].keys():
            print(f"ALBUM: {keys} TRACK: {params[elem][keys]}")
