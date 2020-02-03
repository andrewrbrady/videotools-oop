#!/usr/local/bin/python3

from datetime import 
import json
import os

class ActivityFile():
    def __init__(self, projectDirectoryPath):
        self.projectDirectoryPath = projectDirectoryPath
        self.logPath = '200_documents/207_logs'

    @property
    def projectActivityFile(self):
        return os.path.join(self.projectDirectoryPath, self.logPath, 'activity-log.json')

    def createNewActivityFile(self):
        if os.path.exists(self.projectActivityFile):
            print('path exists')
        else:
            try:
                print('making directory')
                open(self.projectActivityFile, 'w')
                
            except:
                print('There was an error')

    def createNewActivity(self, action, datetime=):
        self.action = action
        self.datetime = datetime
        data = {
            "action": a
            }
        }
        
        try:
            open(self.projectActivityFile, "a")
        except:
            print('failed, creating activity file')
            self.createNewActivityFile()
            
        with open(self.projectActivityFile, "a") as write_file:
                json.dump(data, write_file)
        
        