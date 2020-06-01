import sys
import os
# getting the home folder of the user
from os.path import expanduser
from pathlib import Path


configfile = expanduser("~") + "/.config/nextbac/nextbac.conf"
configpath = Path(configfile)


# checks if config file exists
def checkConfig():
    return configpath.is_file()


# function looks for config file with specified
# backup- and serverpath and returns them
def getConfig():
    with open(configfile) as f:
        content = f.read().splitlines()
    f.close()
    return (content[0], content[1])


def makeConfig():
    print("not implemented yet")
