"""
Get song info.
"""
import shutil
import os
import mpd

from . import brainz
from . import util


def init(port=6600):
    """Initialize mpd."""
    client = mpd.MPDClient()

    try:
        client.connect("localhost", port)
        return client

    except ConnectionRefusedError:
        print("error: Connection refused to mpd/mopidy.")
        os._exit(1)  # pylint: disable=W0212


def get_art(cache_dir, size, client, verbose):
    """Get the album art."""
    song = client.currentsong()

    if len(song) < 2:
        if(verbose): print("album: Nothing currently playing.")
        return

    file_name = f"{song['artist']}_{song['album']}_{size}.jpg".replace("/", "")
    file_name = cache_dir / file_name

    if file_name.is_file():
        shutil.copy(file_name, cache_dir / "current.jpg")
        if(verbose): print("album: Found cached art.")

    else:
        if(verbose): print("album: Downloading album art...")

        brainz.init()
        album_art = brainz.get_cover(song, verbose, size)

        if album_art:
            util.bytes_to_file(album_art, cache_dir / file_name)
            util.bytes_to_file(album_art, cache_dir / "current.jpg")

            if(verbose): print(f"album: Swapped art to {song['artist']}, {song['album']}.")
