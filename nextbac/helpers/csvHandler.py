import os
import csv
import shutil


# format of dict : {key: Image Name, values: [year, month, status]}
def readCsv(backupPath):
    picDict = {}
    with open(backupPath + "/database.csv", mode='r') as picCsv:
        csvReader = csv.DictReader(picCsv)
        for row in csvReader:
            picDict[row['img_name']] = [
                row['year'], row['month'], row['status']
            ]
        picCsv.close()
        return picDict


def writeCsv(backupPath, picDict):
    with open(backupPath + '/database.csv', mode='a') as backupCsv:
        csvWriter = csv.writer(backupCsv, delimiter=',',
                               quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for picName in picDict:
            csvWriter.writerow([
                picName, picDict[picName][0], picDict[picName][1], picDict[picName][2]
            ])
        backupCsv.close()


def changeStatus(backupPath, removePics, status):
    csvReader = csv.reader(open(backupPath + "/database.csv"))
    picLines = list(csvReader)
    for line in picLines:
        if line[0] in removePics:
            line[3] = status

    csvWriter = csv.writer(open(backupPath + "/database.csv", 'w'))
    csvWriter.writerows(picLines)
