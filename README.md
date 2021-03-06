# AudioInfo Tool
Shows audio file information. Supports MP3 and FLAC (under development).

### Installation

Until I have a PyPI package.

```
    $ git clone https://github.com/JuanjoSalvador/AudioInfo-Tool.git
    $ cd AudioInfo-Tool
    $ sudo pip install -r requirements.txt
    $ chmod +x ainfo.py
```

### Usage

```
 $ ./ainfo.py <option> /path/to/file
```

| Option | Description |
|--------|-------------|
| -t     | Shows only technical info |
| -f     | Shows all info available |
| -i     | Shows ID metatags |

Sample output for `ainfo -t ~/my.mp3`

```
    File: my.mp3
    Audio offset: 0
    Bitrate: 192 kbps
    Encoder: LAME 3.96.1+
    Filesize: 2184381
    Layer: 3
    Length: 1.52 minutes
    Mode: 1
    MPEG version: 1
```
### TO DO
* Create pip package
* Add more audio codecs
* Optimizing code

### License

MIT License

