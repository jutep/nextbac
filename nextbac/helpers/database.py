# Handles everything in the database
import shutil
import os


# Checks all Pictures in serverPath folder for new Pictures to store
# they get added to toStorePics variable with year and month and returned
def getPics(path, storedPics, month, year):
    toStorePics = {}
    for filename in os.listdir(path):
        if filename not in storedPics:
            toStorePics[filename] = [year, month, "s"]
    return toStorePics


# stores the Pictures and sends write to database request
def storePictures(serverPath, localPath, pics, month, year, csv_name):
    print(pics)
    for pic_name, pic_value in pics.items():
        sPath = serverPath
        lPath = localPath
        shutil.copyfile(serverPath + "/" + pic_name,
                        localPath + "/" + year + "/" + month + "/" + pic_name)
    print(str(len(pics)) + " pictures stored")
