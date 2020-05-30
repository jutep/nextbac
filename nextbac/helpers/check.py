# Script has function to check the correct folder structure
import os


# checks if correct structure exists
# arguments: path of the backuped directory, currentYear, currentMonth
# if a directory does not exist it will be created
def checkStructure(path, month, year):
    if not os.path.isdir(path + "/" + year):
        os.mkdir(path + "/" + year)
        os.mkdir(path + "/" + year + "/" + month)
        print("folders: " + year + ", " + month + " created")
    elif not os.path.isdir(path + "/" + year + "/" + month):
        os.mkdir(path + "/" + year + "/" + month)
        print("folder: " + month + " created")
