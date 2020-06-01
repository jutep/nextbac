import nextbac.helpers.csvHandler as csvH
import nextbac.helpers.database as db
import nextbac.helpers.check as check
import nextbac.helpers.ownDate as ownDate
import nextbac.helpers.config as config


# main function to direct everything
def backupStart():
    if not config.checkConfig():
        config.makeConfig()
    serverPath, backupPath = config.getConfig()
    csv_name = csvH.check_csv(backupPath)
    month, year = ownDate.currentDate()
    check.checkStructure(backupPath, month, year)
    storedPics = csvH.read_csv(backupPath, csv_name)
    toStorePics = db.getPics(serverPath, storedPics, month, year)
    if toStorePics:
        db.storePictures(serverPath, backupPath,
                         toStorePics, month, year, csv_name)
        csvH.write_csv(backupPath, toStorePics, csv_name)
    else:
        print("nothing to store")
