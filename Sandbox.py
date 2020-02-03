#!/usr/local/bin/python3

from MMFile import ImageFile as IF
from MMFile import VideoFile as VF
from MMFile import MMFile as MMF
from MMFile import AudioFile as AF
from MMFolder import MMFolder as MMF
from Project import Project as Project
from ProjectConfig import ProjectConfigFile as PCF
from ProjectActivity import ActivityFile as ActivityFile

def main():

    # print(mnv.fileBasename)
    # print(mnv.filePath)
    # print(mnv.size)
    # mnv.renameFile('new_file.mov')
    # mnv.openFile(mnv.filePath)
    # mnv.transcode()
    # mnv.transcribe()

    # mni = IF('/Users/andrewbrady/Desktop/asset1.png')
    # print(mni.dimensions)
    # mni.openFile(mni.filePath)

    # mna = AF('/Users/andrewbrady/Desktop/asset1.png')
    # mnf = MMF('/Users/andrewbrady/Desktop/image_sandbox/')
    # mnf = MMF('/Users/andrewbrady/Desktop/sandbox')

    # mnf.transcodeVideo()

    mnv = VF('/Users/andrewbrady/Desktop/sandbox/00082.mov')
    mnv.resize()
    # projPath = '/Users/andrewbrady/Desktop/database/OTR/OTR103'
    # myProject = Project(projPath)
    
    # print(mp.projectConfigFilePath)

    # mpc = PCF(projPath)

    # mpc.createNewConfigFile()


    # print(mpc)

    




if __name__ == "__main__":
    main()








