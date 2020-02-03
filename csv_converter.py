#!/usr/local/bin/python3

import json
import sys

# sys.setdefaultencoding("UTF-8") #set the encode to utf8

fileInput = '/Volumes/GoogleDrive/My Drive/Clients/OTR/OTR103/200_documents/207_logs/activity-log.json'
fileOutput = '/Volumes/GoogleDrive/My Drive/Clients/OTR/OTR103/200_documents/207_logs/activity-log.csv'
inputFile = open(fileInput) #open json file
outputFile = open(fileOutput, 'w') #load csv file
data = json.load(inputFile) #load json content
inputFile.close() #close the input file
output = csv.writer(outputFile) #create a csv.write
output.writerow(data[0].keys())  # header row
for row in data:
    output.writerow(row.values()) #values row