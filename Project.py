#!/usr/local/bin/python3

import os
from ProjectGenerator import Generator


logPath = '200_documents/207_logs'



class Project():


    def __init__(self, projectPath):
        self.projectPath = projectPath

    def beginSession(self):
        # Database entry, and begin working on project
        print('Beginning session')

    def endSession(self):
        # Activity Log entry, end working project
        pass

    @property
    def fullVideoProjectDirectory(self):
        self.videoProjectPath = '600_edit/603_master'
        # self.projectCode = self.projectPath.split('/')[-1]
        return os.path.join(self.projectPath, self.videoProjectPath)

    @property
    def fullVideoProjectPath(self):
        self.videoProjectPath = '600_edit/603_master'
        self.projectCode = self.projectPath.split('/')[-1]
        return os.path.join(self.projectPath, self.videoProjectPath, f'{self.projectCode}.prproj')
        
    @property
    def projectConfigFilePath(self):
        
        return os.path.join(self.projectPath, logPath, 'project-config.json')

    @property
    def activityFilePath(self):
        return os.path.join(self.projectPath, logPath, 'activity-log.json')

    @property
    def projectCreationDate(self):
        pass

    @property
    def projectLastModified(self):
        # Last activity recorded with ProjectActivity
        pass
    
    @property
    def backupDirectories(self):
        pass
    
    @property
    def hoursWorked(self):
        pass
    
    @property
    def projectRate(self):
        pass

    @property
    def favoriteFolders(self):
        pass

    @property
    def remoteFrameProjectLink(self):
        pass




def main():
    print(f'Starting your new file!')

if __name__ == "__main__":
    main()