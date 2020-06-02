# Script has function to check the correct folder structure
import os
import sys
from os.path import expanduser
from pathlib import Path


configfile = expanduser("~") + "/.config/nextbac/nextbac.conf"
configpath = Path(configfile)


def checkConfig():
    return configpath.is_file()


def getConfig():
    with open(configfile) as f:
        content = f.read().splitlines()
    f.close()
    return (content[0], content[1])


def makeConfig():
    print("not implemented yet")


# checks and creates the proper folder structure in backupPath
def checkStructure(path, month, year):
    if not os.path.isdir(path + "/" + year):
        os.mkdir(path + "/" + year)
        os.mkdir(path + "/" + year + "/" + month)
        print("folders: " + year + ", " + month + " created")
    elif not os.path.isdir(path + "/" + year + "/" + month):
        os.mkdir(path + "/" + year + "/" + month)
        print("folder: " + month + " created")
