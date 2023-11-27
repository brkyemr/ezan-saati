import sys
from pydub import AudioSegment
from pydub.playback import play
import json
import os
from datetime import datetime, timedelta
import pytz
import time

# Load audio files from environment variables
sabah_sound_path = os.getenv("SABAH_SOUND_PATH", "/Users/berkayemir/Desktop/ezan/sabah.mp3")
ogle_sound_path = os.getenv("OGLE_SOUND_PATH", "/Users/berkayemir/Desktop/ezan/ogle.mp3")
ikindi_sound_path = os.getenv("IKINDI_SOUND_PATH", "/Users/berkayemir/Desktop/ezan/ikindi.mp3")
aksam_sound_path = os.getenv("AKSAM_SOUND_PATH", "/Users/berkayemir/Desktop/ezan/aksam.mp3")
yatsi_sound_path = os.getenv("YATSI_SOUND_PATH", "/Users/berkayemir/Desktop/ezan/yatsi.mp3")

# Load namazvakti.json from environment variable
json_file_path = os.getenv("JSON_FILE_PATH", "/Users/berkayemir/Desktop/ezan/namazvakti.json")

# Load audio files
sabah_sound = AudioSegment.from_mp3(sabah_sound_path)
ogle_sound = AudioSegment.from_mp3(ogle_sound_path)
ikindi_sound = AudioSegment.from_mp3(ikindi_sound_path)
aksam_sound = AudioSegment.from_mp3(aksam_sound_path)
yatsi_sound = AudioSegment.from_mp3(yatsi_sound_path)

# Load namazvakti.json
with open(json_file_path, "r") as f:
    data = json.load(f)

while True:
    now = datetime.now(pytz.timezone('Europe/Istanbul'))
    today_time = data["times"][f"{now.year}-{now.month}-{now.day}"]

    # Format current time
    current_time = now.strftime("%H:%M")
    print("current_time", current_time)
    print("now", now)

    # Check if the current time matches prayer times
    if current_time in today_time:
        index = today_time.index(current_time)
        print(today_time)

        # Play corresponding sound based on prayer time
        if index == 0:
            play(sabah_sound)
        elif index == 2:
            play(ogle_sound)
        elif index == 3:
            play(ikindi_sound)
        elif index == 4:
            play(aksam_sound)
        elif index == 5:
            play(yatsi_sound)

    time.sleep(10)
