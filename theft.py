#!/usr/bin/env/ python3

import subprocess

# Install youtube-dl
from subprocess import call
call(["sudo", "curl", "-L", "https://yt-dl.org/downloads/latest/youtube-dl", "-o", "/usr/local/bin/youtube-dl"])
call(["sudo", "chmod", "a+rx", "/usr/local/bin/youtube-dl"])

# Install avconv
call(["sudo", "apt-get", "install", "libav-tools"])

# Switch to Music
call(["cd"])
call(["cd", "Music"])

# Ask user for the youtube video url
link = input("Enter the url for the youtube video: ")

# Download video
from subprocess import call
call(["youtube-dl", "--extract-audio", "--audio-format", "mp3", "--output", "\"%(uploader)s%(title)s.%(ext)s\"", link])
