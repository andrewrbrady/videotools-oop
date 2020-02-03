#!/usr/local/bin/python3

from MMFile import ActivityFile
from MMFile import ProjectConfigFile
from MMFolder import MMFolder as MMF
from Project import Project as Project
from ProjectConfig import ProjectConfigFile

def makeNewProject(path):
    newProject = Project(path)
    newProject.generateTemplate()
    newProjectConfigFile = ProjectConfigFile.createNewConfigFile()
    newProjectConfigFile.setProjectConfigDefaults()
    newProjectActivityFile = ActivityFile.createNewActivity(f'Created new project at {newProject.projectPath}')
    newProject.beginSession()

def main():
    projPath = '/Users/andrewbrady/Desktop/database/OTR/OTR104'
    makeNewProject(projPath)


if __name__ == "__main__":
    main()








