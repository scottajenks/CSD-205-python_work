# 8-7. Album
def make_album(artist_name, album_title, tracks=None):
    '''Return a dictionary of information about an album'''
    album_info = {"Artist Name": artist_name, "Album Title": album_title}
    if tracks:
        album_info["Track Count"] = tracks
    return album_info


album1 = make_album("Scott Jenks", "Somethings Goes Pop")
album2 = make_album("Luiz Soares", "Classical All The Way", "18")

print(album1)
print(album2)
print(make_album("Brandi Watterson", "Nothing But Country", "13"))
