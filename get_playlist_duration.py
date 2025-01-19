from pytube import Playlist, YouTube
from datetime import timedelta

def get_playlist_duration(playlist_url):
    playlist = Playlist(playlist_url)
    total_duration = 0

    for video_url in playlist.video_urls:
        video = YouTube(video_url)
        print(f"Video Title: {video.title}")
        print(f"Duration: {format_duration(video.length)}")
        print("-" * 30)
        total_duration += video.length

    return total_duration

def format_duration(seconds):
    return str(timedelta(seconds=seconds))

if __name__ == "__main__":
    playlist_url = input("Enter the URL of the YouTube playlist: ")
    total_duration = get_playlist_duration(playlist_url)

    print(f"Total duration of the playlist: {format_duration(total_duration)}")
