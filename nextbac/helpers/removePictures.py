import os
from .csvHandler import changeStatus


def backupAndServer(backupPath, serverPath, removePics):
    for pic, val in removePics.items():
        os.remove(backupPath + "/" + val[0] + "/" + val[1] + "/" + pic)
        os.remove(serverPath + "/" + pic)
    changeStatus(backupPath, removePics, 'r')
    print('Removing Pictures completed')
