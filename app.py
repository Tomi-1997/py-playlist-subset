import json
import yt_dlp
from Parser import Parser

# URL of playlist, make sure it a url of a playlist, not of a video.
MY_URL = "https://music.youtube.com/playlist?list=RDCLAK5uy_neriXH6JbZPr7Pf4LOi5bGQP-_lWRZXs4"


# I want videos with an overall length of 8:30 minutes
MINUTES = 8
SECONDS = 30


# Plus minus seconds. For example, 8:30 +- 5 seconds.
# Set 0 to get as close as possible.
GIVE_OR_TAKE = 5


# Keep only 8:30 to 8:35
GIVE_ONLY = True


# Exclude videos with less than 60 seconds
NOT_LESS_THAN = 60


##
##
T = MINUTES * 60 + SECONDS
EPS = GIVE_OR_TAKE
_P = Parser()

def main():
    ydl_opts = {
        'match_filter': longer_than,
        'quiet': True,
        'noplaylist': True,
        'extract_flat': True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:

        playlist_info = ydl.extract_info(MY_URL, download=False)

        print(f'Playlist Owner: {playlist_info["channel"]}')
        videos = playlist_info['entries']
        for video in videos:
            title = video['title']
            duration = video['duration']  # In seconds
            url = video['url']
            _P.add_entry(title, duration, url)

        _P.search(T, EPS= EPS, EPS_BIGGER= GIVE_ONLY)


def longer_than(info, *, incomplete):
    """Download only videos longer than a minute (or with unknown duration)"""
    duration = info.get('duration')
    if duration and duration < NOT_LESS_THAN:
        return 'The video is too short'

if __name__ == '__main__':
    main()