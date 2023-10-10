import os 
from youtube_transcript_api import YouTubeTranscriptApi
import re
import requests
from pytube import Playlist

def play2text(playlist_url):
    try:
        playlist = Playlist(playlist_url)
        playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

        video_links = [f"https://www.youtube.com{url}" for url in playlist.video_urls]

        if video_links:
            print("\nVideo Links in the Playlist:")
            with open("links.txt", "a") as f:
                for idx, link in enumerate(video_links, start=1):
                    f.write(link + "\n")
        else:
            print("No video links found in the playlist.")
    except Exception as e:
        print("Error:", e)

