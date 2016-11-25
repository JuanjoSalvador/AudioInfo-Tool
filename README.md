# ainfo
Shows audio file information. Supports MP3 (FLAC under development).

### Basic usage

```
 $ ainfo <option> /path/to/file.mp3
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
