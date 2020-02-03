#!/usr/local/bin/python3

import os

logPath = '200_documents/207_logs'

class Project():

    def __init__(self, projectRoot):
        self.projectRoot = projectRoot

    @property
    def projectConfigFilePath(self):
        
        return os.path.join(self.projectRoot, logPath, 'project-config.json')

    @property
    def activityFilePath(self):
        return os.path.join(self.projectRoot, logPath, 'activity-log.json')

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

    def startTimer(self):
        pass

    def endTimer(self):
        pass




def main():
    print(f'Starting your new file!')

if __name__ == "__main__":
    main()