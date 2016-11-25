#!/usr/bin/env python

import sys, os
from mutagen.mp3 import MP3
from magic import Magic

# Return true if is an audio file
def isAudio(file):
    isAudio = False
    try:
        mime = Magic(mime=True)
        mimetype = mime.from_file(file)
        typeOfFile = mimetype.split("/")
        
        if typeOfFile[0] == "audio":
            isAudio = True
        else:
            print sys.argv[2], "is not a valid file"
    except IOError:
        print sys.argv[2], "is not a valid file or it doesn't exist."
    
    return isAudio

def technical(file):
    audio = MP3(file)
    print "File:", os.path.basename(file)
    print "Bitrate:", audio.info.bitrate
    print "Channels:", audio.info.channels
    print "Encoder:", audio.info.encoder_info
    print "Mode:", audio.info.mode
    print "MPEG version:", audio.info.version
    print "Layer:", audio.info.layer
    print "Length:", round (audio.info.length / 60, 2), "minutes"

def full():
    print "Not implemented yet."

def needHelp():
    print "Do you need help? Try ainfo --help"

try:
    if len(sys.argv) > 1:
        if sys.argv[1] == "-t":
            technical(sys.argv[2])
        elif len(sys.argv) > 1 and sys.argv[1] == "-f":
            if isAudio(sys.argv[2]):
                full()
except IndexError:
    needHelp()