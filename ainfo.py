#!/usr/bin/env python

import sys, mp3
from magic import Magic

# VERSION
VERSION = "0.2-Dev"

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


    tag = TinyTag.get(file)
    audio = MP3(file)

    # Get minutes and seconds
    m, s = divmod(int(audio.info.length), 60)
    h, m = divmod(m, 60)

    print BOLD + "Album:" + END, tag.album
    print BOLD + "Album artist:" + END, tag.albumartist
    print BOLD + "Artist:" + END, tag.artist
    print BOLD + "Audio offset:" + END, tag.audio_offset
    print BOLD + "Bitrate:" + END, tag.bitrate, "kbps"
    print BOLD + "Disc:" + END, tag.disc 
    print BOLD + "Encoder:" + END, audio.info.encoder_info
    print BOLD + "File:" + END, os.path.basename(file)
    print BOLD + "Filesize:" + END, round((float(tag.filesize)/1024)/1024,2), "MiB"
    print BOLD + "Genre:" + END, tag.genre
    print BOLD + "Layer:" + END, audio.info.layer
    # Minutes and seconds
    if h > 0:
        print BOLD + "Length:" + END, "%02dh %02dm %02ds" % (h, m, s)
    else:
        print BOLD + "Length:" + END, "%02dm %02ds" % (m, s)

    print BOLD + "Mode:" + END, audio.info.mode
    print BOLD + "MPEG version:" + END, audio.info.version
    print BOLD + "Title:" + END, tag.title
    print BOLD + "Track:" + END, tag.track
    print BOLD + "Year:" + END, tag.year
    
    

def showHelp():
    print BOLD + '\033[4m' + "AudioInfo Tool v" + VERSION + END
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
    if len(sys.argv) > 1:
        if sys.argv[1] == "-t":
            mp3.technical(sys.argv[2])
        elif len(sys.argv) > 1 and sys.argv[1] == "-f":
            if isAudio(sys.argv[2]):
                mp3.full(sys.argv[2])
        elif len(sys.argv) > 1 and sys.argv[1] == "-i":
            if isAudio(sys.argv[2]):
                mp3.idtags(sys.argv[2])
        elif len(sys.argv) > 1 and sys.argv[1] == "--help":
            showHelp()
        else:
            needHelp()
except IndexError:
    needHelp()