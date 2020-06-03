# Script has function to check the correct folder structure
import os
import sys
from os.path import expanduser
from pathlib import Path
from .inputHandler import configInput


configPath = expanduser("~") + "/.config/nextbac"
configFile = configPath + "/nextbac.conf"


def checkConfig():
    return os.path.exists(configFile)


def getConfig():
    with open(configFile) as f:
        content = f.read().splitlines()
    f.close()
    return (content[0], content[1])


def makeConfig():
    serverPath, backupPath = configInput()
    if not os.path.isdir(configPath):
        os.mkdir(configPath)
    # Creating the configfile
    newConf = open(configFile, "w+")
    newConf.write(serverPath + "\n")
    newConf.write(backupPath)
    newConf.close()
    print("config file created")


# checks and creates the proper folder structure in backupPath
def checkStructure(backupPath, month, year):
    if not os.path.isdir(backupPath + "/" + year):
        os.mkdir(backupPath + "/" + year)
        os.mkdir(backupPath + "/" + year + "/" + month)
        print("folders: " + year + ", " + month + " created")
    elif not os.path.isdir(backupPath + "/" + year + "/" + month):
        os.mkdir(backupPath + "/" + year + "/" + month)
        print("folder: " + month + " created")
