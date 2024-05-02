def create_playlist(playlist_name: str, *song_titles)->dict:
    playlist = {
        "name": playlist_name,
        "songs": set(song_titles)
    }
    return playlist


playlist1 = create_playlist("Workout Mix", "Eye of the Tiger", "Stronger", "Lose Yourself")
print(playlist1)

