from pydub import AudioSegment


song = AudioSegment.from_wav("../cache/voices0.wav")

print (song.duration_seconds)

song.duration_seconds = song.duration_seconds * 0.8

print (song.duration_seconds)
