import os
import csv
import shutil


# format of dict : {key: Image Name, values: List(year, month, status)}
def readCsv(backupPath, file_name):
    picDict = {}
    with open(backupPath + "/" + file_name, mode='r') as picCsv:
        csvReader = csv.DictReader(picCsv)
        for row in csvReader:
            picDict[row['img_name']] = [
                row['year'], row['month'], row['status']
            ]
        picCsv.close()
        return picDict


# return: existing or created csv filename
def checkCsv(backupPath):
    picCsv = os.listdir(backupPath)
    for file in picCsv:
        if file.endswith(".csv"):
            return file
    else:
        with open(os.path.join(backupPath, "picDictbase.csv"), 'w') as newCsv:
            newCsv.write("img_name,year,month,status\n")
        print("database created")
        return "picDictbase.csv"


def writeCsv(backupPath, picDict, picCsv):
    with open(backupPath + '/' + picCsv, mode='a') as backupCsv:
        csvWriter = csv.writer(backupCsv, delimiter=',',
                               quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for picName in picDict:
            csvWriter.writerow([
                picName, picDict[picName][0], picDict[picName][1], picDict[picName][2]
            ])
        backupCsv.close()
