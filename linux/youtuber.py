import sys
from pytubefix import YouTube
from pytubefix.cli import on_progress

if len(sys.argv) < 2:
	print("Need URL - python3 youtuber.py https://youtube.com/watch?v=...")
	exit()

url = sys.argv[1]

print("Checking URL...")
yt = YouTube(url, on_progress_callback=on_progress, use_oauth=True, allow_oauth_cache=True)

print("Finding best resolution...")
ys = yt.streams.filter(type="video").order_by("resolution").last()

print("Downloading...")
ys.download()

