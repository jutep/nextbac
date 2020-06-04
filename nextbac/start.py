import nextbac.helpers.csvHandler as csvHandler
import nextbac.helpers.database as db
import nextbac.helpers.check as check
import nextbac.helpers.ownDate as ownDate
import nextbac.helpers.removePictures as removePictures


def backup():
    month, year = ownDate.currentDate()
    backupPath, serverPath = check.checkStructure(month, year)
    storedPics = csvHandler.readCsv(backupPath)
    toStorePics = db.getPics(serverPath, storedPics, month, year)
    if toStorePics:
        db.storePictures(serverPath, backupPath,
                         toStorePics, month, year)
        csvHandler.writeCsv(backupPath, toStorePics)
    else:
        print("nothing to store")


def remove(removePics):
    serverPath, backupPath = check.getConfig()
    removePics = check.picsExist(removePics, serverPath, backupPath)
    print(removePics)
    removePictures.backupAndServer(
        backupPath, serverPath, removePics)
