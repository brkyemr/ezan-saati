from pydub import AudioSegment
from pydub.playback import play

sound = AudioSegment.from_mp3("sabah.mp3")
play(sound)
