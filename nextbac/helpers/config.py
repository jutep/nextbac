import sys
import os

# getting the home folder of the user
from os.path import expanduser
home = expanduser("~")


# checks if config file exists
def checkConfig():
    pass


# function looks for config file with specified
# backup- and serverpath and returns them
def getConfig():
    with open(home + '/.config/nextbac/nextbac.conf') as f:
        content = f.read().splitlines()
    f.close()
    return (content[0], content[1])


def makeConfig(localPath, cloudPath):
    pass
