import os
import sys
from os.path import expanduser
from pathlib import Path
from .inputHandler import configInput
from .csvHandler import readCsv


configPath = expanduser("~") + "/.config/nextbac"
configFile = configPath + "/nextbac.conf"


# checkking config, folder structure in backupPath and csv file existance
def checkStructure(month, year):
    if not checkConfig():
        makeConfig()
    serverPath, backupPath = getConfig()
    if checkPath(serverPath, backupPath):
        backupStructure(backupPath, month, year)
        checkCsv(backupPath)
        return (backupPath, serverPath)
    else:
        raise Exception("One of your configured Paths does not exist anymore")


def checkPath(serverPath, backupPath):
    return True if (os.path.isdir(serverPath)
                    and os.path.isdir(backupPath)) else False


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


def checkCsv(backupPath):
    if not os.path.exists(backupPath + "/database.csv"):
        with open(os.path.join(backupPath, "database.csv"), 'w') as newCsv:
            newCsv.write("img_name,year,month,status\n")
            newCsv.close()
        print("database created")


def backupStructure(backupPath, month, year):
    if not os.path.exists(backupPath + "/" + year):
        os.mkdir(backupPath + "/" + year)
        os.mkdir(backupPath + "/" + year + "/" + month)
        print("folders: " + year + ", " + month + " created")
    elif not os.path.exists(backupPath + "/" + year + "/" + month):
        os.mkdir(backupPath + "/" + year + "/" + month)
        print("folder: " + month + " created")


# returns a dict with the values of the pictures like year, month, status
def picsExist(removePics, serverPath, backupPath):
    storedPics = readCsv(backupPath)
    picsWithValues = {}
    for pic in removePics:
        if not (pic in storedPics):
            raise ValueError('Picture does not exist in backup: ' + pic)
        elif not os.path.isfile(serverPath + "/" + pic):
            raise ValueError('File does not exist in server: ' + pic)
        else:
            picsWithValues[pic] = storedPics[pic]

    return picsWithValues


def difference(serverPath, backupPath):
    storedPics = readCsv(backupPath)
    differencePics = {}
    for pic, val in storedPics.items():
        if val[2] == "s":
            if not (os.path.exists(serverPath + "/" + pic)):
                differencePics[pic] = val

    return differencePics
