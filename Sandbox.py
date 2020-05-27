#!/usr/local/bin/python3

from MMFile import ActivityFile
from MMFile import ProjectConfigFile
from MMFolder import MMFolder as MMF
from Project import Project as Project
from ProjectConfig import ProjectConfigFile
import os

def makeNewProject(path):
    newProject = Project(path)
    newProject.generateTemplate()
    newProjectConfigFile = ProjectConfigFile.createNewConfigFile()
    newProjectConfigFile.setProjectConfigDefaults()
    newProjectActivityFile = ActivityFile.createNewActivity(f'Created new project at {newProject.projectPath}')
    newProject.beginSession()

def main():
    
    MMF(os.getcwd()).transcode()
    # MMF(os.getcwd()).downloadDummyImages()

if __name__ == "__main__":
    main()

