# Script has function to check the correct folder structure
import os
import sys
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

# checks if correct structure exists
# arguments: path of the backuped directory, currentYear, currentMonth
# if a directory does not exist it will be created


def checkStructure(path, month, year):
    if not os.path.isdir(path + "/" + year):
        os.mkdir(path + "/" + year)
        os.mkdir(path + "/" + year + "/" + month)
        print("folders: " + year + ", " + month + " created")
    elif not os.path.isdir(path + "/" + year + "/" + month):
        os.mkdir(path + "/" + year + "/" + month)
        print("folder: " + month + " created")
