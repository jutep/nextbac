# Handles everything in the database
import shutil
import os


# only returns not already stored pictures
def getPics(path, storedPics, month, year):
    toStorePics = {}
    for filename in os.listdir(path):
        if filename not in storedPics:
            toStorePics[filename] = [year, month, "s"]
    return toStorePics


def storePictures(serverPath, localPath, pics, month, year):
    for name in pics:
        shutil.copyfile(serverPath + "/" + name,
                        localPath + "/" + year + "/" + month + "/" + name)
    print(str(len(pics)) + " pictures stored")
