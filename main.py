import sys
from pydub import AudioSegment
from pydub.playback import play
import json
import os
from datetime import datetime, timedelta
import pytz
import time

# Define dynamic base path (you can set this dynamically based on your requirements)
base_path = os.getenv("BASE_PATH", "/home/hayalezan/ezansaati/")

# Load audio files from environment variables
sabah_sound_path = os.path.join(base_path, "sabah.mp3")
ogle_sound_path = os.path.join(base_path, "ogle.mp3")
ikindi_sound_path = os.path.join(base_path, "ikindi.mp3")
aksam_sound_path = os.path.join(base_path, "aksam.mp3")
yatsi_sound_path = os.path.join(base_path, "yatsi.mp3")

# Load namazvakti.json from environment variable
json_file_path = os.path.join(base_path, "namazvakti.json")
# Load audio files
sabah_sound = AudioSegment.from_mp3(sabah_sound_path)
sabah_sound = sabah_sound + 10  # Increase volume by 10 decibels

ogle_sound = AudioSegment.from_mp3(ogle_sound_path)
ogle_sound = ogle_sound + 10

ikindi_sound = AudioSegment.from_mp3(ikindi_sound_path)
ikindi_sound = ikindi_sound + 10

aksam_sound = AudioSegment.from_mp3(aksam_sound_path)
aksam_sound = aksam_sound + 10

yatsi_sound = AudioSegment.from_mp3(yatsi_sound_path)
yatsi_sound = yatsi_sound + 10

# Load namazvakti.json
with open(json_file_path, "r") as f:
    data = json.load(f)

while True:
    now = datetime.now(pytz.timezone('Europe/Istanbul'))
    formatted_key = now.strftime('%Y-%m-%d')
    # today_time = data["times"][f"{now.year}-{now.month}-{now.day}"]
    today_time = data["times"][formatted_key]
    # Format current time
    current_time = now.strftime("%H:%M")
   
    # Check if the current time matches prayer times
    if current_time in today_time:
        index = today_time.index(current_time)

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
