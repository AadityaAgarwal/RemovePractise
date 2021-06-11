import time
import shutil
import os
path = input("Enter the path: ")
timeCalc = time.time()-(30*24*3600)
check = os.path.exists(path)
listFile = os.listdir(path)


def getTime(fileName):
    ctime = os.stat(fileName).st_ctime
    return ctime


def removeFolder(path):
    shutil.rmtree(path)


def removeFile(path):
    os.remove(path)


def main():

    if(check == True):

        for rootFolder, files, folders in os.walk(path):
            if(timeCalc >= getTime(rootFolder)):
                removeFolder(rootFolder)
                break
            else:
                for folder in folders:
                    folderPath = os.path.join(rootFolder, folder)
                    if(timeCalc > getTime(folderPath)):
                     removeFolder(folderPath)

                for file in files:
                    filePath = os.path.join(rootFolder, file)
                    if(timeCalc > getTime(filePath)):
                      removeFile(filePath)
    else:
        print("Path not found!")
