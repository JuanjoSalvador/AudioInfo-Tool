from mutagen.mp3 import MP3
import sys
import magic

# Return true if is an audio file
def isAudio(file):
    import magic
    mime = magic.Magic(mime=True)
    mimetype = mime.from_file(file)
    isAudio = False
    typeOfFile = mimetype.split("/")
    if typeOfFile[0] == "audio":
        isAudio = True
    
    return isAudio

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

def needHelp():
    print "Do you need help? Try ainfo --help"


if len(sys.argv) > 1:
    if sys.argv[1] == "-t":
        if isAudio(sys.argv[2]):
            technical(sys.argv[2])
        else:
            print sys.argv[2], "is not an valid file."

    elif len(sys.argv) > 1 and sys.argv[1] == "-f":
        if isAudio(sys.argv[2]):
            full()
        else:
            print sys.argv[2], "is not an valid file."

    else:
        needHelp()
else:
    needHelp()