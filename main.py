from ytmusicapi import YTMusic
import logging


logging.basicConfig(filename='logger.log', encoding='utf-8', level=logging.INFO)
ytmusic = YTMusic("headers.json")


playlist_name = input('Playlist name: ')
playlist_description = input('Playlist_description: ')
playlistId = ytmusic.create_playlist(playlist_name, playlist_description)
logging.info(f'\n Created Playlist: {playlist_name} with ID {playlistId}')

file_path = input('Path to file: ')
logging.info(f'Path to file: {file_path}')

with open(file_path, "r") as f:
    playlist = f.read()
playlist_list = playlist.split(sep="\n")
for item in playlist_list:
    try:
        search_results = ytmusic.search(item)
        ytmusic.add_playlist_items(playlistId, [search_results[0]["videoId"]])
        logging.info(f"{item}: Success")
    except (KeyError, IndexError):
        logging.info(f"{item}: Error")


