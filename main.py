import sys
from pydub import AudioSegment
from pydub.playback import play
import json
import os
from datetime import datetime
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

# Load and boost volume of audio files (+10 dB)
sabah_sound = AudioSegment.from_mp3(sabah_sound_path).apply_gain(+10)
ogle_sound = AudioSegment.from_mp3(ogle_sound_path).apply_gain(+10)
ikindi_sound = AudioSegment.from_mp3(ikindi_sound_path).apply_gain(+10)
aksam_sound = AudioSegment.from_mp3(aksam_sound_path).apply_gain(+10)
yatsi_sound = AudioSegment.from_mp3(yatsi_sound_path).apply_gain(+10)

# Load namazvakti.json
json_file_path = os.path.join(base_path, "namazvakti.json")
with open(json_file_path, "r") as f:
    data = json.load(f)

# Main loop
while True:
    now = datetime.now(pytz.timezone('Europe/Istanbul'))
    formatted_key = now.strftime('%Y-%m-%d')
    
    # Get today's prayer times
    today_time = data["times"][formatted_key]
    
    # Format current time as HH:MM
    current_time = now.strftime("%H:%M")
    print("current_time:", current_time)
    print("now:", now)

    # Check if the current time matches any prayer time
    if current_time in today_time:
        index = today_time.index(current_time)
        print("Prayer times today:", today_time)

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

    # Sleep 10 seconds before checking again
    time.sleep(10)
