import os
from .csvHandler import changeStatus


def removePictures(backupPath, serverPath, removePics):
    for pic, val in removePics.items():
        os.remove(backupPath + "/" + val[0] + "/" + val[1] + "/" + pic)
        os.remove(serverPath + "/" + pic)
    changeStatus(backupPath, removePics, 'r')
    print('Removing Pictures completed')


def removeInBackup(backupPath, removePics):
    for pic, val in removePics.items():
        print(pic)
        os.remove(backupPath + "/" + val[0] + "/" + val[1] + "/" + pic)
    changeStatus(backupPath, removePics, 'r')
    print('Difference to server completed')
