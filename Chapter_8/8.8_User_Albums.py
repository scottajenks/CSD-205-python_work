# 8-8. User Albums
def make_album(artist_name, album_title):
    '''Return a dictionary of information about an album'''
    album_info = {"Artist Name": artist_name, "Album Title": album_title}
    return album_info


while True:
    print("Who is your favorite recording artist and favorite album of theirs?")
    print("\tEnter 'q' to quit at anytime.")

    art_name = input("Artist Name: ")
    if art_name == 'q':
        break
    album_name = input("Album Title: ")
    if album_name == 'q':
        break

    names = make_album(album_name, art_name)
    print(f"I cannot wait to listen to {album_name} by {art_name}!")
