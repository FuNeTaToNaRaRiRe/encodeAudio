# Audio Encode

Some scripts to make audio encoding easier.

## Prerequisites

- eac3to       (https://www.videohelp.com/software/eac3to)
- flac         (https://xiph.org/flac/index.html)
- qaac         (https://github.com/nu774/qaac)
- ffmpeg       (https://www.ffmpeg.org/download.html)

## Usage:

python encodeAudio.py --arg path.

-W or --wav  -> Use this if you need to convert audio from a .m2ts file.
-F or --flac -> Use this to convert .wav file to .flac.
-A or --aac  -> Use this to convert .wav and .flac file to .m4a.

## Licensing

- MIT

## TODO

- Ask user to specify track number for .m2ts file (it converts only the first audio by default).