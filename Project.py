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
        
    def generateTemplate(self):
        print('Generating Template...')
        Generator.run()
        # Create file structure with symlinked items

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




def main():
    print(f'Starting your new file!')

if __name__ == "__main__":
    main()