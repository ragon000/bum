# 🎵 bum-urxvt

[![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE.md)

`bum-urxvt` is a daemon that downloads album art for songs playing in `mpd`/`mopidy` and displays them as the background image of the `urxvt` terminal window it was started in. `bum-urxvt` doesn't loop on a timer, instead it waits for `mpd`/`mopidy` to send a `player` event. When it receives a `player` event it wakes up and downloads album art for the current playing track. This makes `bum-urxvt` lightweight and makes it idle at `~0%` CPU usage.

`bum-urxvt` uses [musicbrainz](https://musicbrainz.org/) to source and download cover art, if an album is missing it's cover art you can easily create an account and fill in the data yourself. `bum-urxvt` outputs (when the verbose option is set) a `release-id` which you can use to find the exact entry on musicbrainz.

Note: `bum-urxvt` is meant to be used with files that don't have embedded album art (`mopidy-spotify`).


![showcase](https://i.imgur.com/62OLmuT.gif)

## Dependencies

- `python 3.6+`
- `python-mpv`
- `python-mpd2`
- `musicbrainzngs`
- `ImageMagick` - Can be removed by deleting a line in `change.sh`

## Installation
- You need urxvt compiled with pixbuf
  - On Arch it's in the [AUR](https://aur.archlinux.org/packages/rxvt-unicode-pixbuf/)
### Arch
```sh
sudo pacman -S imagemagick git
git clone https://github.com/ragon000/bum-urxvt/
cd bum-urxvt
pip3 install --user .
cd ..
rm -rf bum-urxvt
```
### Ubuntu/Debian
```sh
sudo apt-get install imagemagick git
git clone https://github.com/ragon000/bum-urxvt/
cd bum-urxvt
pip3 install --user .
cd ..
rm -rf bum-urxvt
```

## Usage

```sh
usage: bum [-h] [--size "px"] [--cache_dir "/path/to/dir"] [--version]
           [--port PORT] [--verbose]

bum-urxvt - Download and display album art for mpd tracks in your terminal.

optional arguments:
  -h, --help            show this help message and exit
  --size "px"           what size to display the album art in.
  --cache_dir "/path/to/dir"
                        Where to store the downloaded cover art. (Defaults to
                        ~/.cache/bum
  --version             Print "bum" version.
  --port PORT           Use a custom mpd port.
  --verbose             Turn on song informations
```


## Donate to the creator of bum

Donations will allow him to spend more time working on `bum`.

If you like `bum` and want to give back in some way you can donate here:

**https://patreon.com/dyla**
