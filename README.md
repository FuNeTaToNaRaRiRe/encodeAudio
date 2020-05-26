# Audio Encode

Some scripts to make audio encoding easier.

## Prerequisites

- eac3to       (https://www.videohelp.com/software/eac3to)
- flac         (https://xiph.org/flac/index.html)
- qaac         (https://github.com/nu774/qaac)
- ffmpeg       (https://www.ffmpeg.org/download.html)

## Usage:

python encodeAudio.py --arg path.

| Arg (big) | Arg (small) | Description |
| :-------: | :---------: | ----------- |
| --help | -H | Show this message and close.
| --wav | - W | Convert audio to .wav (Use this on a m2ts file).
| --track | -T | Chose track of .m2ts file (use only if more than 1 audio track)
| --flac | -F | Convert audio (from .wav) to .flac.
| --aac | - A | Convert audio (from .wav or .flac)to .m4a.
| --recursive | -R | If used, will check all the subfolders of the main folder.
| x | x | Path to the file/folder. If none, will use the current folder.

## Licensing

- MIT
