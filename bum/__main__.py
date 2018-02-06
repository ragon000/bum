"""
'||
 || ...  ... ...  .. .. ..
 ||'  ||  ||  ||   || || ||
 ||    |  ||  ||   || || ||
 '|...'   '|..'|. .|| || ||.

Created by Dylan Araps
"""
import argparse
import pathlib
from pathlib import Path
import os
from . import song

from .__init__ import __version__


def get_args():
    """Get the script arguments."""
    description = "bum-urxvt - Download and display album art \
                   for mpd tracks in your terminal."
    arg = argparse.ArgumentParser(description=description)

    arg.add_argument("--size", metavar="\"px\"",
                     help="what size to display the album art in.",
                     default=250)

    arg.add_argument("--cache_dir", metavar="\"/path/to/dir\"",
                     help="Where to store the downloaded cover art. (Defaults to ~/.cache/bum",
                     default=pathlib.Path.home() / ".cache/bum")

    arg.add_argument("--version", action="store_true",
                     help="Print \"bum\" version.")

    arg.add_argument("--port",
                     help="Use a custom mpd port.",
                     default=6600)
    arg.add_argument("--verbose",
                     help="Turn on song informations",
                     action="store_true")
    return arg.parse_args()


def process_args(args):
    """Process the arguments."""
    if args.version:
        print(f"bum {__version__}")
        exit(0)


def main():
    """Main script function."""
    args = get_args()
    process_args(args)
    
    client = song.init(args.port)

    while True:
        song.get_art(args.cache_dir, args.size, client, args.verbose)
        os.system(str(Path(__file__).resolve().parent)+"/change.sh " + str(args.cache_dir.resolve()) + "/current.jpg")
        client.send_idle()

        if client.fetch_idle(["player"]):
          if(args.verbose):
              print("album: Received player event from mpd. Swapping cover art.")
          continue


if __name__ == "__main__":
    main()
