# py-playlist-subset
*Generate a list of songs with requsted length, from a youtube playlist.*

Do you also sometimes jog not with a spotwatch, but until your playlist ends? No? <br>
Okay, if you still want to, you can input a public playlist, and how long you need, and get a result pretty quick.

## Example
Let's say I want some songs from YouTube's 'Cozy Jazz' playlist, with a total length of 17 minutes. <br>
I will input:
```
URL = "https://music.youtube.com/playlist?list=RDCLAK5uy_neriXH6JbZPr7Pf4LOi5bGQP-_lWRZXs4"
M = 17
S = 0
```
And this is one of the results, nice!
```
Duration: 160, Title: Mar-cia                                           , Url: https://music.youtube.com/watch?v=cK7Vqo6VZjI
Duration: 374, Title: Day Dream                                         , Url: https://music.youtube.com/watch?v=hld5v6lX448
Duration: 199, Title: Gone With The Wind                                , Url: https://music.youtube.com/watch?v=fEAUWfKx7eQ
Duration: 289, Title: Torn                                              , Url: https://music.youtube.com/watch?v=t6Pzi-MSsAc
Seconds Overall: 1022
```
## Usefulness
<br><br><br>
## Installation
1. Install yt-dlp from https://github.com/yt-dlp/yt-dlp for the video info extraction.
2. Set in the app.py file these variables:
    - Url of your playlist
    - Requested minutes
    - Requested seconds

    You can also tweak those:
    - Error margin for a close result
    - Error margin to apply only above requested time
    - Ignore short videos

3. Run app.py! 🥳


The above variables match this code block at the start of app.py, respectively
```
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
```

## How it works
We generate a random group of elements of size X, a lot of times.
If the sum of their durations is close to our target, great.

### How we pick X
Let's say we want a list of around 600 seconds. <br>
Our average is 200 for a song. So we divide the target by the average. <br>
```
  # Approxmiate number of items needed to reach target
        approx = T / (self.avg)
```
X = 3, Let's generate groups of size 3.
<br>
This works, but for a playlist with videos of varied length, we do the following: <br>
Calculate the standard deviation. <br>
Judging by the result, we decide to include more or less items in our random group. <br>
```
        # High variance? try to include even less, or even more items
        plusminx = self.std / T

        # To Ints
        approx = int(approx)
        plusminx = int(plusminx)

        # Limits
        approx = max(approx, 1)
        plusminx = max(plusminx, 1)
```
With this addition, we will generate groups with 2 to 4 elements.
## Correctness Proof
<br>
<br>
<br>
<br>
<br>
