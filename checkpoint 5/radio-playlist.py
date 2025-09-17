
weekly_playlist = ["Blinding Lights","Levitating","As It Was", "Heat Waves","Good 4 u"]
weekly_playlist.append("Drivers License")
weekly_playlist.insert(0, "Bohemian Rhapsody")
weekly_playlist.remove("Good 4 u")

print(weekly_playlist[0:])
print(weekly_playlist.index("Levitating"))
print(weekly_playlist.count("As It Was"))
print(weekly_playlist.reverse())
print(weekly_playlist.sort())