#!/usr/bin/env/python

from datetime import datetime
import time
import json
import os
from PIL import Image
import subprocess

class MMFile():
    def __init__(self, path):
        self.fileWOExtension, self.fileExtension = os.path.splitext(self.filePath)
        self.fileBasename = os.path.basename(self.filePath)
        self.size = os.path.getsize(path)

    def renameFile(self, newFileBasename):
        print(f'Renaming {fileBasename} to {newFileBasename}')

    def openFile(self, path):
        print(f'Opening file {self.filePath}')  

class VideoFile(MMFile):
    def __init__(self, path):
        MMFile.__init__(self, path)
        self.hasAlpha = ''
        self.dimensions = ''
        self.codec = ''
        self.hasTranscript = ''
        self.transcriptPath = ''
        self.duration = ''

    def transcode(self, options):
        print('Transcoding video!')
        self.opts = options
        self.videoConvert(self.opts[0], self.opts[1])
        
    def returnOptions(self):
        ans=True
        while ans:
            print (r"""
            1.MP4
            2.ProResProxy
            3.ProResHQ
            4.MP3
            5.WAV
            6.H265
            7.1080P Proxy
            """)
            self.ans=input("What would you like to do? ") 
            if self.ans=="1": # Basic H264 MP4
                self.output_format = 'mp4'
                self.options = ['-pix_fmt', 'yuv420p']
            elif self.ans=="2": # ProRes Proxy
                self.output_format = 'mov'
                self.options = ['-c:v', 'prores', '-profile:v', '0', '-c:a', 'copy']
            elif self.ans=="3": # ProRes HQ
                self.output_format = 'mov'
                self.options = ['-c:v', 'prores', '-profile:v', '3']
            elif self.ans=="4": # MP3
                self.output_format = 'mp3'
                self.options = ['-vn', '-ar', '44100', '-ac', '2', '-ab', '192k', '-f', 'mp3']
            elif self.ans=="5": # WAV
                self.output_format = 'wav'
                self.options = ['-vn', '-ar', '96000', '-ac', '2', '-ab', '256k', '-f', 'wav']
            elif self.ans=="6": # H265 MP4
                self.output_format = 'mp4'
                self.options = ['-c:v', 'hevc', '-preset', 'slow', '-crf', '23', '-tag:v', 'hvc1', '-an']
            elif self.ans=="7": # ProRes Proxy
                self.output_format = 'mov'
                self.options = ['-c:v', 'prores', '-profile:v', '0', '-vf', 'scale=-1:1080', '-c:a', 'copy']
                
            else:
                print("\n Not Valid Choice Try again")
            return self.options, self.output_format
            # break

  
    def videoConvert(self,options,output_format):
        # print(self.options)
        self.proxy_directory = f'{os.getcwd()}/{output_format}' # Takes output format and lists it as the directory for the files to be exported into
        self.output_file = f'{self.proxy_directory}/{self.fileBasename.split(".")[0]}.{output_format}' # Takes output format and creates the new path for the exported file
        ffmpeg_array = ['ffmpeg', '-i', self.filePath, self.output_file] # The basic FFMPEG array without any options
        self.starting_position = 3 # Notes where the options should be inserted into the FFMPEG arguments
        for option in options: # Begin for loop inserting each option argument into the FFMPEG array
            ffmpeg_array.insert(self.starting_position, option) 
            self.starting_position += 1 # Increment the position of where the next element should be inserted into the array
        if os.path.exists(self.proxy_directory): # Check if export directory already exists. If so, begin exporting into this directory
            subprocess.call(ffmpeg_array) # Run the FFMPEG command via subprocess
        else: # If the export directory does not exist
            os.mkdir(self.proxy_directory) # Create export directory
            subprocess.call(ffmpeg_array) # Run the FFMPEG command via subprocess
        
    def transcribe(self):
        print('Transcribing video!')

    def resize(self):
        newActivity = ActivityFile('/Users/andrewbrady/Development/sandbox/client_directory_sandbox/OTR/OTR103')
        newActivity.createNewActivity(f'Resized {self.filePath}')
        print('Resizing video!')
    
    def addBumper(self, order, objects):
        print('Adding bumper!')

    def addOverlay(self, overlayPath):
        print('Adding overlay!')

    def openTranscript(self):
        print(f'Opening Transcript: {self.transcriptPath}')

class ImageFile(MMFile):
    def __init__(self, path):
        MMFile.__init__(self, path)
        self.isVector = ''

    @property
    def hasAlpha(self):
        im = Image.open(self.filePath, 'r')
        return im.mode == 'RGBA'

    @property
    def dimensions(self):
        im = Image.open(self.filePath)
        width, height = im.size
    
        return [width, height]

    def resize(self):
        print(f'Resizing image: {self.filePath}')
        im = Image.open(self.filePath, 'r')
        return im.size

    def addOverlay(self):
        print('Adding overlay!')

class ProjectFile(MMFile):
    def __init__(self, path):
        MMFile.__init__(self, path)

    def openBackupDirectory(self):
        print('Opening backup')

    def openProject(self):
        print('Opening project!')


    @property
    def lastModified(self):
        print('Last modified')

class AudioFile(MMFile):
    def __init__(self,path):
        MMFile.__init__(self,path)

    def formatType(self):
        print('Audio format')

    def convert(self):
        print('Converting audio file')

    @property
    def hasTranscript(self):
        return None

class DocumentFile(MMFile):
    def __init__(self, path):
        MMFile.__init__(self,path,type)
        self.type = type
        
    @property
    def relatedPaths(self):
        return "Here is an arry of all related paths"

class ActivityFile(DocumentFile):

    def __init__(self, path):
        MMFile.__init__(self,path)
        self.projectDirectoryPath = path
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

    def createNewActivity(self, action, datetime=datetime.fromtimestamp(time.time())):
        self.action = action
        self.datetime = datetime
        data = {
            "action": f'{self.action}',
            "datetime": f'{self.datetime}'
            }
            
        try:
            open(self.projectActivityFile, "a")
        except:
            print('failed, creating activity file')
            self.createNewActivityFile()
            
        with open(self.projectActivityFile, "a") as write_file:
                json.dump(data, write_file)

class ProjectConfigFile(DocumentFile):
    def __init__(self):
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

    def setProjectConfigDefaults(self, mode=1):
        # Edit project-config.json to have default values
        pass
    
    def editConfigFile(self):
        pass

    def updateRate(self):
        # Update unit rate (i.e. day, hour, etc.) for project
        pass

    def updateHoursWorked(self):
        pass