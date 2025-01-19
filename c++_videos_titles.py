from pathlib import Path
from pytube import Playlist
from re import sub

pl = Playlist("https://youtube.com/playlist?list=PLDoPjvoNmBAwy-rS6WKudwVeb_x63EzgS&si=DeM_XYV_2KGzybt4")
for video in pl.videos:
  title = video.title
  title = sub(r"\s|-|,", "_",title[title.find("With C++ ") + 10:]).replace("___", "_").replace("__", "_")
  print(title)
  Path(f"/home/ghoudiy/Documents/Programming/C++/Fundamentals_Of_Programming/Course/Not_yet/{title}.cpp").touch()