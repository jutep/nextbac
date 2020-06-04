import os


def configInput():
    print("Configuration for Nextbac")
    print()
    print("Notice ~/.config/ needs to exist")
    print("Pls enter your full server path like /home/USER/...")
    dirName = False
    while(not dirName):
        serverPath = input()
        if os.path.exists(serverPath):
            dirName = True
        else:
            print("Wrong filepath enter again")
    print()
    print("Enter your full backup path like /home/USER/...")
    dirName = False
    while(not dirName):
        backupPath = input()
        if os.path.exists(backupPath):
            dirName = True
        else:
            print("Wrong filepath enter again")

    return (serverPath, backupPath)
