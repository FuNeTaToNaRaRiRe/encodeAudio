import subprocess as sp
import shlex
import os
import argparse
import glob
import sys

extensionsTuple = (".m2ts", ".wav", ".flac")

def wavEncode(filePath):
    sp.run(
        shlex.split(
            f"eac3to \"{filePath}\" -log=NUL \"{os.path.splitext(filePath)[0]}.wav\""
        )
    )

def wavEncode2(filePath, trackNumber):
    sp.run(
        shlex.split(
            f"eac3to \"{filePath}\" -log=NUL {trackNumber}:\"{os.path.splitext(filePath)[0]}_Track{trackNumber}.wav\"" 
        )
    )

def flacEncode(filePath):
    sp.run(
        shlex.split(
            f"eac3to \"{filePath}\" -log=NUL \"{os.path.splitext(filePath)[0]}.flac\""
        )
    )

def aacEncode(filePath):
    sp.run(
        shlex.split(
            f"ffmpeg -i \"{filePath}\" -loglevel panic \"{os.path.splitext(filePath)[0]}.wav\""
        )
    )
    sp.run(
        shlex.split(
            f"qaac \"{os.path.splitext(filePath)[0]}.wav\" -V 127 --no-delay \"{os.path.splitext(filePath)[0]}.m4a\""
        )
    )
    os.remove(f"{os.path.splitext(filePath)[0]}.wav")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-R", "--recursive", action="store_true", default=False, help="Check files recurcively if your path is a folder.")
    parser.add_argument("-W", "--wav", action="store_true", default=False, help="Encode a PCM file, use this with .m2ts files.")
    parser.add_argument("-T", "--track", action="store_true", type=int, default=False, help="Track number to encode.")
    parser.add_argument("-F", "--flac", action="store_true", default=False, help="Enable  FLAC encoding.")
    parser.add_argument("-A", "--aac", action="store_true", default=False, help="Enable AAC encoding.")
    parser.add_argument("path", metavar="path", type=str, nargs="?", help="Path of the file/folder you want to use")
    args = parser.parse_args()

    if args.path == None:
        print(f"[ERROR] Usage: python {sys.argv[0]} -ARG/--arg path")
        sys.exit(1)

    if args.wav:
        if os.path.isfile(args.path):
            if args.track:
                wavEncode2(args.path, args.track)
            wavEncode(args.path)
        else:
            if args.recurcive:
                fileList = glob.glob(f"{args.path}/**/*", recursive=True)
            else:
                fileList = glob.glob(f"{args.path}/*")
            for audioFile in fileList:
                if audioFile.endswith(extensionsTuple[0]):
                    wavEncode(audioFile)

    if args.flac:
        if os.path.isfile(args.path):
            flacEncode(args.path)
        else:
            if args.recurcive:
                fileList = glob.glob(f"{args.path}/**/*", recursive=True)
            else:
                fileList = glob.glob(f"{args.path}/*")
            for audioFile in fileList:
                if audioFile.endswith(extensionsTuple):
                    flacEncode(audioFile)

    if args.aac:
        if os.path.isfile(args.path):
            aacEncode(args.path)
        else:
            if args.recurcive:
                fileList = glob.glob(f"{args.path}/**/*", recursive=True)
            else:
                fileList = glob.glob(f"{args.path}/*")
            for audioFile in fileList:
                if audioFile.endswith(extensionsTuple):
                    aacEncode(audioFile)
