#!/usr/bin/env python

import sys, os
from tinytag import TinyTag
from mutagen.mp3 import MP3
from magic import Magic

# Format vars
BOLD =  '\033[1m'
END  =  '\033[0m'

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
    tag = TinyTag.get(file)
    audio = MP3(file)
    print BOLD + "File:" + END, os.path.basename(file)
    print BOLD + "Audio offset:" + END, tag.audio_offset
    print BOLD + "Bitrate:" + END, tag.bitrate, "kbps"
    print BOLD + "Encoder:" + END, audio.info.encoder_info
    print BOLD + "Filesize:" + END, tag.filesize
    print BOLD + "Layer:" + END, audio.info.layer
    print BOLD + "Length:" + END, round (audio.info.length / 60, 2), "minutes"
    print BOLD + "Mode:" + END, audio.info.mode
    print BOLD + "MPEG version:" + END, audio.info.version

def idtags(file):
    tag = TinyTag.get(file)
    print BOLD + "Album:" + END, tag.album
    print BOLD + "Album artist:" + END, tag.albumartist
    print BOLD + "Artist:" + END, tag.artist
    print BOLD + "Disc:" + END, tag.disc 
    print BOLD + "Genre:" + END, tag.genre
    print BOLD + "Title:" + END, tag.title
    print BOLD + "Track:" + END, tag.track
    print BOLD + "Year:" + END, tag.year

def full(file):
    tag = TinyTag.get(file)
    audio = MP3(file)
    print BOLD + "Album:" + END, tag.album
    print BOLD + "Album artist:" + END, tag.albumartist
    print BOLD + "Artist:" + END, tag.artist
    print BOLD + "Audio offset:" + END, tag.audio_offset
    print BOLD + "Bitrate:" + END, tag.bitrate, "kbps"
    print BOLD + "Disc:" + END, tag.disc 
    print BOLD + "Encoder:" + END, audio.info.encoder_info
    print BOLD + "File:" + END, os.path.basename(file)
    print BOLD + "Filesize:" + END, tag.filesize
    print BOLD + "Genre:" + END, tag.genre
    print BOLD + "Layer:" + END, audio.info.layer
    print BOLD + "Length:" + END, round (audio.info.length / 60, 2), "minutes"
    print BOLD + "Mode:" + END, audio.info.mode
    print BOLD + "MPEG version:" + END, audio.info.version
    print BOLD + "Title:" + END, tag.title
    print BOLD + "Track:" + END, tag.track
    print BOLD + "Year:" + END, tag.year
    
    

def showHelp():
    print "This is the HELP menu"

def needHelp():
    print "Do you need help? Try ainfo --help"

try:
    if len(sys.argv) > 1:
        if sys.argv[1] == "-t":
            technical(sys.argv[2])
        elif len(sys.argv) > 1 and sys.argv[1] == "-f":
            if isAudio(sys.argv[2]):
                full(sys.argv[2])
        elif len(sys.argv) > 1 and sys.argv[1] == "-i":
            if isAudio(sys.argv[2]):
                idtags(sys.argv[2])
        elif len(sys.argv > 1) and sys.argv[1] == "--help":
            showHelp()
        else:
            needHelp()
except IndexError:
    needHelp()