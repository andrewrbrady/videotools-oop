#!/usr/local/bin/python3

import os
import subprocess

def main():
  youtube_url = input("YouTube URL")
  start_time = int(input("Start Time"))
  end_time = int(input("End Time"))
  duration = end_time - start_time
  output_filename = input("Output Filename?")
  output_path = os.path.join(os.getcwd(), output_filename + '.mp4')
  print(f'YTURL: {youtube_url}, Start: {start_time}, End: {end_time}, Duration: {duration} Output: {output_path}')
  command = f'ffmpeg $(youtube-dl -g {youtube_url} -f bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio | sed "s/.*/-ss {start_time} -i &/") -t {duration} -c copy {output_path}' 
  command_split = command.split(' ')
  print(command_split)
  subprocess.call(command_split)

if __name__ == '__main__':
    main()
