# ainfo
Shows audio file information. Supports MP3 (FLAC under development).

### Basic usage

```
 $ python ainfo.py <option> /path/to/file.mp3
```

| Option | Description |
|--------|-------------|
| -t     | Shows only technical info |
| -f     | Default. Shows all info available |
| -i     | Shows ID metatags |

Sample output for `ainfo -t my.mp3`


```
 Bitrate: 192158 
 Channels: 2
 Encoder: LAME 3.96.1+
 Mode: 1
 MPEG version: 1
 Layer: 3
 Length: 1.52 minutes
```
