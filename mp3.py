import os
from tinytag import TinyTag
from mutagen.mp3 import MP3

BOLD      = '\033[1m'
UNDERLINE = '\033[4m'
END       = '\033[0m'

def technical(file):
    tag = TinyTag.get(file)
    audio = MP3(file)

    # Get minutes and seconds
    m, s = divmod(int(audio.info.length), 60)
    h, m = divmod(m, 60)

    print BOLD + "File:" + END, os.path.basename(file)
    print BOLD + "Audio offset:" + END, tag.audio_offset
    print BOLD + "Bitrate:" + END, int(tag.bitrate), "kbps"
    print BOLD + "Channels:" + END, audio.info.channels
    print BOLD + "Encoder:" + END, audio.info.encoder_info
    print BOLD + "Filesize:" + END, round((float(tag.filesize)/1024)/1024,2), "MiB"
    print BOLD + "Layer:" + END, audio.info.layer
    # Minutes and seconds
    if h > 0:
        print BOLD + "Length:" + END, "%02dh %02dm %02ds" % (h, m, s)
    else:
        print BOLD + "Length:" + END, "%02dm %02ds" % (m, s)

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

    # Get minutes and seconds
    m, s = divmod(int(audio.info.length), 60)
    h, m = divmod(m, 60)

    print BOLD + "Album:" + END, tag.album
    print BOLD + "Album artist:" + END, tag.albumartist
    print BOLD + "Artist:" + END, tag.artist
    print BOLD + "Audio offset:" + END, tag.audio_offset
    print BOLD + "Bitrate:" + END, int(tag.bitrate, "kbps")
    print BOLD + "Channels:" + END, audio.info.channels
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