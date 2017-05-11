#!/usr/bin/env python3

import subprocess

from subprocess import call

call(["/usr/bin/ruby", "-e", "$(curl", "-fsSL", "https://raw.githubusercontent.com/Homebrew/install/master/install)"])

call(["brew", "install", "libav"])

call(["sudo", "curl", "-L", "https://yt-dl.org/downloads/latest/youtube-dl", "-o", "/usr/local/bin/youtube-dl"])

call(["sudo", "chmod", "a+rx", "/usr/local/bin/youtube-dl"])

link = input("Enter the url for the youtube video: ")

call(["youtube-dl", "--extract-audio", "--audio-format", "mp3", "--output", "\"%(uploader)s%(title)s.%(ext)s\"", link])
