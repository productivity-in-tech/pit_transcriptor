import mutagen.flac
import sys

filename = sys.argv[1]

audio = mutagen.flac.Open(filename)
print(audio.info.length/60)
