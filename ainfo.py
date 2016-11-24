from mutagen.mp3 import MP3
import sys

def technical(a):
    audio = MP3(a)
    print "Bitrate:", audio.info.bitrate
    print "Channels:", audio.info.channels
    print "Encoder:", audio.info.encoder_info
    print "Mode:", audio.info.mode
    print "MPEG version:", audio.info.version
    print "Layer:", audio.info.layer
    print "Length:", round (audio.info.length / 60, 2), "minutes"

def full():
    print "Not implemented yet."

if sys.argv[1] == "-t":
    technical(sys.argv[2])
else:
    full()