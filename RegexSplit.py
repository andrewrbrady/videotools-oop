#!/usr/local/bin/python3
import json
import re

def removeTimecode(text):
    try:
        pattern = re.compile(r'\[[A-Za-z0-9\S]{8}]')
        search = re.split(pattern, text)
        clean_text = ''
        for s in search:
            clean_text += s.lstrip()
        return clean_text
    except:
        pass

def lineArray(transcript):
    line_arr = {}
    for idx, val in enumerate(transcript):
        if idx % 2 == 0:
            cur_val = val.strip()
            split_val = re.split(':\s', cur_val)
            pattern = re.compile(r'\[[0-9]{2}:[0-9]{2}:[0-9]{2}\]')
            search = re.search(pattern, split_val[1])
            if search == None:
                timecode_status = False
                timecode = None 
            else:
                timecode_status = True
                timecode = search[0]
                timecode = timecode[1:-1]
            tmp = {"speaker"=split_val[0], "text"=removeTimecode(split_val[1].strip()), "status"=timecode_status, "timecode"=timecode}
            line_arr.update(tmp)
        else:
            pass

    return line_arr

def writeJSON(location):
    trans = open('/Users/andrewbrady/Desktop/KTC1007_S001_S001_T001.txt')
    data = lineArray(trans)
    with open(location, 'w') as outfile:
        json.dump(data, outfile)
    
writeJSON('/Users/andrewbrady/Desktop/data.json')