from MMFile import VideoFile as VF
from MMFile import ImageFile as IF
from FfmpegBlade import run as FFRun
from UnsplashDownloader import ImageBatch as IB
from ProjectGenerator import Generator as PG
from pathlib import Path
import os

class MMFolder():
    def __init__(self,path):
        self.directoryPath = path
        self.directoryBasename = self.directoryPath.split('/',-1)
        self.isAllVideos = None
        self.isAllImages = None
        self.parentPath = os.path.dirname(self.directoryPath)
        self.allFilesLength = len(self.allFiles)

    @property
    def allFiles(self):
        my_list = list()
        for f in os.listdir(self.directoryPath):
            if not f.startswith('.'):
                my_list.append(f)
        
        return my_list

    @property
    def fullVideoProjectDirectory(self):
        self.videoProjectPath = '600_edit/603_master'
        # self.projectCode = self.projectPath.split('/')[-1]
        return os.path.join(self.directoryPath, self.videoProjectPath)

    @property
    def fullVideoProjectPath(self):
        self.videoProjectPath = '600_edit/603_master'
        self.projectCode = self.directoryPath.split('/')[-1]
        return os.path.join(self.directoryPath, self.videoProjectPath, f'{self.projectCode}.prproj')

    @property
    def fullAEProjectPath(self):
        self.AEProjectPath = '700_AE/704_master'
        self.projectCode = self.directoryPath.split('/')[-1]
        return os.path.join(self.directoryPath, self.AEProjectPath, f'{self.projectCode}.aep')

    @property
    def remoteProjectDirectory(self):
        # localDirectoryParentBasename = os.path.basename(self.directoryPath) # Get name of containing folder (Client Code)
        self.remoteDriveProjectFolder = os.path.join(Path.home(), 'Desktop/gdrive/Clients', self.directoryPath.split('/')[-2], self.directoryPath.split('/')[-1])
        return self.remoteDriveProjectFolder

    def runMethod(self):
        self.list = self.allFiles
        for x in range(len(self.list)):
            returnOpts = VF(currentFile).returnOptions()
            currentFile = os.path.join(self.directoryPath,self.list[x])
            VF(currentFile).transcode(returnOpts)

    def lowerCaseAllExtensions(self):
        files = self.allFiles
        for f in files:
            f = IF(f)
            path, ext = os.path.splitext(f.filePath)
            if ext.isupper():
                os.rename(f.filePath, path + ext.lower())

    def transcode(self):
        FFRun('loop') 
        
    def downloadDummyImages(self, maxImages=4, width=800, height=600):
        IB(maxImages, width, height).run()

    
    def createProjectStructure(self):
        print(self.directoryPath)
        PG(self.directoryPath).run()
    