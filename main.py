import pygame
import json
import time
from datetime import datetime, timedelta
import pytz

# Initialize Pygame
pygame.init()

# Load audio files
sabah_sound = pygame.mixer.Sound("/home/hayalezan/ezan-saati/sabah.mp3")
ogle_sound = pygame.mixer.Sound("/home/hayalezan/ezan-saati/ogle.mp3")
ikindi_sound = pygame.mixer.Sound("/home/hayalezan/ezan-saati/ikindi.mp3")
aksam_sound = pygame.mixer.Sound("/home/hayalezan/ezan-saati/aksam.mp3")
yatsi_sound = pygame.mixer.Sound("/home/hayalezan/ezan-saati/yatsi.mp3")

# Load namazvakti.json
with open("/home/hayalezan/ezan-saati/namazvakti.json", "r") as f:
    data = json.load(f)

# Initialize a dictionary to keep track of whether each prayer time has been played
played_flag = {0: False, 2: False, 3: False, 4: False, 5: False}

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

        # Check if the sound for the current prayer time has not been played
        if not played_flag[index]:
            # Play corresponding sound based on prayer time
            if index == 0:
                pygame.mixer.Sound.play(sabah_sound)
            elif index == 2:
                pygame.mixer.Sound.play(ogle_sound)
            elif index == 3:
                pygame.mixer.Sound.play(ikindi_sound)
            elif index == 4:
                pygame.mixer.Sound.play(aksam_sound)
            elif index == 5:
                pygame.mixer.Sound.play(yatsi_sound)

            # Set the flag to indicate that the sound has been played
            played_flag[index] = True

    # Reset flags at midnight to allow sounds to be played again on the next day
    if now.hour == 0 and now.minute == 0:
        played_flag = {0: False, 2: False, 3: False, 4: False, 5: False}

    time.sleep(10)
