# script for handling the csv file
import os
import csv
import shutil


# reading the csv file path to the directory need to be given
# returns a dictionary in the format:
# key: Image Name, values: List(year, month, status)
def read_csv(path, file_name):
    data = {}
    with open(path + "/" + file_name, mode='r') as backupCsv:
        csv_reader = csv.DictReader(backupCsv)
        for row in csv_reader:
            data[row['img_name']] = [row['year'], row['month'], row['status']]
        backupCsv.close()
        return data


# checks if a csv file exists in local directory if not creates one
# return: existing or created csv filename
def check_csv(path):
    src = os.listdir(path)
    for file in src:
        if file.endswith(".csv"):
            return file
    else:
        with open(os.path.join(path, "database.csv"), 'w') as csv_file:
            csv_file.write("img_name,year,month,status\n")
        print("database created")
        return "database.csv"


# Writing to the backup csv file
# given the path to the file directory and
# a dictionary to store the files. Dictonary should have format:
# key: Image Name, values: List(year, month, status)
# path should be the backup path
def write_csv(path, picturesToStore, csv_name):
    with open(path + '/' + csv_name, mode='a') as backupCsv:
        csv_writer = csv.writer(backupCsv, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for pic in picturesToStore:
            csv_writer.writerow([pic, picturesToStore[pic][0],
                                 picturesToStore[pic][1],
                                 picturesToStore[pic][2]])
        backupCsv.close()
