#!/usr/local/bin/python3

import concurrent.futures
import os
import time

def loop():
    def process_video(curFile):
        print(f'Starting! {curFile}')
        # if not f.startswith('.') and os.path.basename(f) is not 'Icon\r': # blocks out .DS_Store & Icon fs
        # 	print('Converting: ' + f)  
        # 	self.videoConvert(f, os.path.splitext(os.path.basename(f))[0], opts[1], opts[0])

    t1 = time.perf_counter()
    # opts = self.returnOptions()
    # print(opts)
    # if opts!=None:
    dirFiles = os.listdir(os.getcwd())
    print(dirFiles)
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(process_video, dirFiles)

    t2 = time.perf_counter()
    
    print(f'Finished in {t2-t1} seconds')

def main():
    loop()    

if __name__ == "__main__":
    main()