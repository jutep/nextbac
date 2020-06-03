import nextbac.helpers.csvHandler as csvHandler
import nextbac.helpers.database as db
import nextbac.helpers.check as check
import nextbac.helpers.ownDate as ownDate


def backupStart():
    month, year = ownDate.currentDate()
    if not check.checkConfig():
        check.makeConfig()
    serverPath, backupPath = check.getConfig()
    picCsv = csvHandler.checkCsv(backupPath)
    check.checkStructure(backupPath, month, year)
    storedPics = csvHandler.readCsv(backupPath, picCsv)
    toStorePics = db.getPics(serverPath, storedPics, month, year)
    if toStorePics:
        db.storePictures(serverPath, backupPath,
                         toStorePics, month, year, picCsv)
        csvHandler.writeCsv(backupPath, toStorePics, picCsv)
    else:
        print("nothing too store")
