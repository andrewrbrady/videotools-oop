#!/usr/local/bin/python3

import os

class ProjectConfigFile():
    def __init__(self, projectDirectoryPath):
        self.projectDirectoryPath = projectDirectoryPath
        self.logPath = '200_documents/207_logs'

    @property
    def projectConfigurationFile(self):
        return os.path.join(self.projectDirectoryPath, self.logPath, 'project-config.json')

        
    def createNewConfigFile(self):
        if os.path.exists(self.projectConfigurationFile):
            print('path exists')
        else:
            try:
                print('making directory')
                open(self.projectConfigurationFile, 'w')
            except:
                print('There was an error')
    
    def editConfigFile(self):
        pass

    def updateRate(self):
        # Update unit rate (i.e. day, hour, etc.) for project
        pass

    def updateHoursWorked(self):
        pass
    

    
    
    # def readConfig():
