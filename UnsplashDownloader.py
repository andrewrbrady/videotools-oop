#!/usr/local/bin/python3

import os
import subprocess
import sys

class ImageBatch():
    def __init__(self, maxImages=4, width=800, height=600):
        try:
            self.max = sys.argv[1]
            self.width = sys.argv[2]
            self.height = sys.argv[3]
        except:
            self.max = maxImages
            self.width = width
            self.height = height

    def downloadImages(self):
        i = 1
        while i <= int(self.max):
            url = f'https://source.unsplash.com/random/{self.width}x{self.height}-{i}.jpg'
            command = ['wget', url]
            subprocess.call(command)
            i += 1

    def run(self):
        try:
            self.downloadImages(int(self.max), int(self.width), int(self.height))    
        except:
            self.downloadImages() 

def main():
    ImageBatch().run()

if __name__ == "__main__":
    main()