import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = 25697525
API_HASH = "3a52c5e4a793c2da23614a90e8e2dac5"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "7440690265:AAEmQEdZFKpy8a9eIa5gsyAymlWFSEEU_C4"

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb+srv://yashsamrat32169:ylWiINR00JzSqwhP@cluster0.j44oov2.mongodb.net/?retryWrites=true&w=majority"

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOG_GROUP_ID = -1002481277537

# Get this value from @ultron2_robot on Telegram by /id
OWNER_ID = 6996610763

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/rishabhops/alice",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = "https://t.me/GROOVYMUSICHERE"
SUPPORT_GROUP = "https://t.me/GROOVYMUSICHERE"

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = "BQGIHPUAjqkXa2ZShkbYPzsvmBQtoZgjSTej93xPpbzL2xhwOUrpENfPSqbMR8Y6aGICq5VLe0WfG0bEiiwDDvbvy8kYdna1gL1eeiqakiiAbCBpjhcxTDBEeCTvpy8yTmNujlYwFoP64Fa-j7pRGRbE5XoRZbd3CqOu3_bNmPThPi0Kj3j3AponZp5dH0WVhQiJoaxiuSQaSQrfz40nv7O3WCjo8xLM8xiwjEjuVYz1Q3fQNP3xbQGpFEVU8ZA88bspneeCKHE5-NNpNWqdCXxUYPXUZ75tGVRjtESBs2cMvDzNsImJeEVsgBCcJ2Uw3YdyRF9zAi_jnAJUwSv3L2_5u8LqYAAAAAGdJ_ZxAA"
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = "https://envs.sh/PX5.jpg"

PING_IMG_URL = "https://envs.sh/PX5.jpg"

PLAYLIST_IMG_URL = "https://envs.sh/PX5.jpg"
STATS_IMG_URL = "https://envs.sh/PX5.jpg"
TELEGRAM_AUDIO_URL = "https://envs.sh/PX5.jpg"
TELEGRAM_VIDEO_URL = "https://envs.sh/PX5.jpg"
STREAM_IMG_URL = "https://envs.sh/PX5.jpg"
SOUNCLOUD_IMG_URL = "https://envs.sh/PX5.jpg"
YOUTUBE_IMG_URL = "https://envs.sh/PX5.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://envs.sh/PX5.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://envs.sh/PX5.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://envs.sh/PX5.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
