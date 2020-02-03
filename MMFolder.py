from MMFile import VideoFile as VF
from MMFile import ImageFile as IF
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

    def transcodeVideo(self):
        files = self.allFiles
        opts = self.returnOptions()
        for f in files:
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
            return [self.options, self.output_format]
            break

  
    def videoConvert(self,options,output_format):
        # print(self.options)
        self.proxy_directory = f'{os.getcwd()}/{output_format}' # Takes output format and lists it as the directory for the files to be exported into
        self.output_file = f'{self.proxy_directory}/{self.fileBasename}.{output_format}' # Takes output format and creates the new path for the exported file
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

    