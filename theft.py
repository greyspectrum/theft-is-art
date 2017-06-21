#!/usr/bin/env/ python3

import subprocess
from subprocess import call
import os
import sys

def query_yes_no(question, default="yes"):
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")

answer = query_yes_no("Would you like to install dependencies? This is only necessary the first time you run this script.")

# Install youtube-dl

call(["sudo", "curl", "-L", "https://yt-dl.org/downloads/latest/youtube-dl", "-o", "/usr/local/bin/youtube-dl"])
call(["sudo", "chmod", "a+rx", "/usr/local/bin/youtube-dl"])

# Install avconv

call(["sudo", "apt-get", "install", "libav-tools"])

# Switch to Music

os.chdir(~/Music)

# Ask user for the youtube video url

link = input("Enter the url for the youtube video: ")

# Download video

call(["youtube-dl", "--extract-audio", "--audio-format", "mp3", "--output", "\"%(uploader)s%(title)s.%(ext)s\"", link])
