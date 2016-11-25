#!/usr/bin/env python

import sys, mp3, flac
from magic import Magic

# VERSION
VERSION = "0.2-Dev"

BOLD      = '\033[1m'
UNDERLINE = '\033[4m'
END       = '\033[0m'

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
            print inputFile, "is not a valid file"
    except IOError:
        print inputFile, "is not a valid file or it doesn't exist."
    
    return isAudio

def typeOfAudio(file):
    mime = Magic(mime=True)
    mimetype = mime.from_file(file)
    typeOfFile = mimetype.split("/")

    return typeOfFile[1]
  
def showHelp():
    print BOLD + UNDERLINE + "AudioInfo Tool v" + VERSION + END
    print ""
    print "USAGE"
    print ""
    print "    ainfo <option> /path/to/my.mp3"
    print ""
    print "OPTIONS"
    print ""
    print "    -f      Shows full info about audio file"
    print "    -t      Shows technical info about file"
    print "    -i      Shows IDv2/IDv3 metatags from file"
    print "    --help  Shows help"
    print ""
    print "AUTHOR"
    print ""
    print "    AudioInfo Tools written by Juanjo Salvador - http://juanjosalvador.es\n    View project on GitHub - http://github.com/JuanjoSalvador/ainfo"
    print ""

def needHelp():
    print "Do you need help? Try ainfo --help"

try:
    inputFile = sys.argv[2]
    option = sys.argv[1]

    if len(sys.argv) > 1:
        # Technical
        if option == "-t":
            if isAudio(inputFile):
                if typeOfAudio(inputFile) == "mp3":
                    mp3.technical(inputFile)
                elif typeOfAudio(inputFile) == "x-flac":
                    flac.technical(inputFile)
        # Full
        elif len(sys.argv) > 1 and option == "-f":
            if isAudio(inputFile):
                if typeOfAudio(inputFile) == "mp3":
                    mp3.full(inputFile)
                elif typeOfAudio(inputFile) == "x-flac":
                    flac.full(inputFile)
        # ID tags
        elif len(sys.argv) > 1 and option == "-i":
            if isAudio(inputFile):
                if typeOfAudio(inputFile) == "mp3":
                    mp3.idtags(inputFile)
                elif typeOfAudio(inputFile) == "x-flac":
                    flac.idtags(inputFile)
        # Help
        elif len(sys.argv) > 1 and option == "--help":
            showHelp()
        else:
            needHelp()
except IndexError:
    needHelp()