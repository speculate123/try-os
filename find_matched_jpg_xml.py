import os
import shutil
import pathlib

DataPath = 'C:/Users/abc/Desktop/RoadDamageDataset/'

allFileList = os.listdir(DataPath)
allFile = os.listdir(DataPath)

allFileListdir = []
for file in allFileList:
    if os.path.isdir(os.path.join(DataPath,file)):
        allFileListdir.append(file)

for file in allFileListdir:
    for xml in os.listdir(os.path.join(DataPath, file, 'Annotations/')):
        shutil.move(os.path.join(DataPath, file, 'Annotations/',xml),os.path.join(DataPath,file,'JPEGImages/'))

for file in allFileListdir:
    shutil.rmtree(os.path.join(DataPath,file,'Annotations'))

for file in allFileListdir:
    items = os.listdir(os.path.join(DataPath, file, 'JPEGImages'))
    jpgs = []
    for names in items:
        if names.endswith(".jpg"):
            jpgs.append(names)
    items = os.listdir(os.path.join(DataPath, file, 'JPEGImages'))
    xmls = []
    for names in items:
        if names.endswith(".xml"):
            xmls.append(names)
    for jpg in jpgs:
        bool = 0
        for xml in xmls:
            if jpg[:-4]==xml[:-4]:
                bool = 1
        if bool == 0:
            noxmldatapath = os.path.join(DataPath,file,'JPEGImages/noxmldata')
            if not os.path.isdir(noxmldatapath):
                os.mkdir(noxmldatapath)
            shutil.move(os.path.join(DataPath, file, 'JPEGImages',jpg),noxmldatapath)
    for xml in xmls:
        bool = 0
        for jpg in jpgs:
            if jpg[:-4]==xml[:-4]:
                bool = 1
        if bool == 0:
            noxmldatapath = os.path.join(DataPath,file,'JPEGImages/noxmldata')
            if not os.path.isdir(noxmldatapath):
                os.mkdir(noxmldatapath)
            shutil.move(os.path.join(DataPath, file, 'JPEGImages',xml),noxmldatapath)
