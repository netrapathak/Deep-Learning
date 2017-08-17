import os
import shutil

#---------------------To define--------------------------------------------#
path = '.././Train'
savePath = '.././Testing'
percentSplit = 0.1
#--------------------------------------------------------------------------#

def moveFile(imgPath, savePath):
    global counter
    if counter < threshold:
        shutil.move(imgPath, savePath)
        counter += 1
        print 'moving',counter
    else:
        return None


folders = os.listdir(path)
for folder in folders:
    folderPath = os.path.join(path,folder)
    saveFolderPath = os.path.join(savePath,folder)
    if (os.path.exists(saveFolderPath) == False):
        os.makedirs(saveFolderPath)
    fileListing = os.listdir(folderPath)
    pathList = map(lambda file: ( folderPath+'/'+file , saveFolderPath+'/'+file), fileListing)
    imgPathList,savePathList = zip(*pathList)

    counter = 0

    trainData = len(fileListing)
    threshold = percentSplit*trainData

    print 'Folder Name: %sTotal Data: %dValidation Data moved: %d'%(folder, trainData, threshold)

    map(moveFile, imgPathList, savePathList)
