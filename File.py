import os

class MMFile:
    __init__(self, path):
        self.filePath = path
        self.fileBasename = os.path.basename(self.filePath)
        self.extension = ''
        self.relativePath = os.path.relpath(path, projectDirectory)    

