#!/usr/local/bin/python3

import concurrent.futures
from concurrent.futures import ProcessPoolExecutor 
import os
import sys
import subprocess
import time

class NewVideoFolder():
	currentDirectory = os.getcwd()
	def __init__(self, command, currentDirectory = currentDirectory):
		self.command = command
		self.currentDirectory = currentDirectory

	def returnOptions(self):
		self.output_format = ''
		self.options = ''
		self.ans=True
		while self.ans:
			print (r"""
1.MP4
2.ProResProxy
3.ProResHQ
4.MP3
5.WAV
6.H265
7.1080P Proxy
8.Cancel
			""")
			self.ans=input("What would you like to do?\n") 
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
			elif self.ans=="8": # Cancel
				return None
			else:
				print("\n Not Valid Choice Try again and again")

			return self.output_format, self.options

	def videoConvert(self, inputFile,outputFileName,options,output_extension):
		self.inputFile = inputFile
		self.outputFileName = outputFileName
		self.options = options
		self.output_extension = output_extension
		self.proxy_directory = os.path.join(str(self.currentDirectory), str(self.output_extension))
		self.output_file = f'{self.proxy_directory}/{outputFileName}.{output_extension}' # Takes output format and creates the new path for the exported file
		self.ffmpeg_array = ['ffmpeg', '-i', self.inputFile, self.output_file] # The basic FFMPEG array without any options
		self.starting_position = 3 # Notes where the options should be inserted into the FFMPEG arguments
		for option in options: # Begin for loop inserting each option argument into the FFMPEG array
			self.ffmpeg_array.insert(self.starting_position, option) 
			self.starting_position += 1 # Increment the position of where the next element should be inserted into the array
		if os.path.exists(self.proxy_directory): # Check if export directory already exists. If so, begin exporting into this directory
			subprocess.call(self.ffmpeg_array) # Run the FFMPEG command via subprocess
		else: # If the export directory does not exist
			os.mkdir(self.proxy_directory) # Create export directory
			subprocess.call(self.ffmpeg_array) # Run the FFMPEG command via subprocess

	
	def process_video(self, curFile, opts):
			# print(f'curFile: {curFile}')
			# print(f'opts: {opts}')
			self.videoConvert(curFile, os.path.splitext(os.path.basename(curFile))[0], opts[1], opts[0])

	def loop(self):
		opts = self.returnOptions()
		t1 = time.perf_counter()
		dirFiles = os.listdir(os.getcwd())
		array = [(dirFiles[i], opts) for i in range(len(dirFiles))]
		with ProcessPoolExecutor() as pool:
			pool.map(self.process_video, *zip(*array))
		t2 = time.perf_counter()
		print(t2-t1)



	def dryLoop(self):
		opts = self.returnOptions()
		if opts!=None:
			for file in os.listdir(self.currentDirectory):
				if not file.startswith('.') and os.path.basename(file) is not 'Icon\r': # blocks out .DS_Store & Icon files
					print('Converting: ' + file)  
					# self.videoConvert(file, os.path.splitext(os.path.basename(file))[0], opts[1], opts[0])

def run(command='loop'):
	myVideoFolder = NewVideoFolder(command)
	if command == 'loop':
		myVideoFolder.loop()
	elif command == 'dry':
		myVideoFolder.dryLoop()

def main():
	run()

	

	

if __name__ == '__main__':
	main()