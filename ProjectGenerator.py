#!/usr/local/bin/python3

from GlobalVariables import GlobalVariables as GV
import json
import os
from pathlib import Path
import re
# from MMFolder import MMFolder as MMF
import shutil

class Generator():
    def __init__(self, projectPath):
        self.projectPath = projectPath

    def check_if_path_exists(self,path):
        if os.path.exists(path):
            print(f'Path: {path} already exists. Continuing the program.')
            pass
        else:
            os.mkdir(path)
            print(f'{path} did not exist. Successfully created the path.')

    # Google Drive Actions en

    def remote_drive_actions(self):
        self.localDirectoryParentBasename = Path(self.projectPath).parent # Get name of containing folder (Client Code)
        self.remoteDriveParentFolder = os.path.join(Path.home(), 'Desktop/gdrive/Clients', self.projectPath.split('/')[-2]) # Join 
        self.check_if_path_exists(self.remoteDriveParentFolder)
        self.remoteDriveProjectFolder = os.path.join(self.remoteDriveParentFolder, self.projectPath.split('/')[-1])
        self.check_if_path_exists(self.remoteDriveProjectFolder)
        os.chdir(self.remoteDriveProjectFolder)
        self.section_assembly(2, "documents", ["legal", "brief", "branding", "scripts", "production_schedule", "invoices", "logs"])
        self.documents_dir = os.path.join(self.remoteDriveProjectFolder, '200_documents')
        os.symlink(self.documents_dir, f'{self.projectPath}/200_documents')
        self.local_recursive_subdirectory_creation_loop(self.read_folder_structure_json_file(), os.getcwd()) # Creates folders which were created on local directory that still need to be created on the remote folder. 
        os.chdir(self.projectPath)

    def check_if_in_project_directory(self):
        print('checking regex')
        self.current_project_regex_check = bool(re.match(r"^[a-zA-Z]{3}\-?\d{3,4}$", os.path.basename(self.projectPath)))
        print('checked regex')
        if self.current_project_regex_check:
            print(r"""

            You are in a project directory which matches a project code.    
            
            """)
        else:
            print(r"""

            You are not in a directory which matches a project code. Please navigate to a project directory with a structure such as 'ARB123', 'ZZZ134', etc.
            
            Exiting program.

            """)
            exit() # End program

    # Section Assembly

    # Argument #1 is the first number of the section level has '00' attached to it. 

    # Argument #2 is the description of the section level. It is attached to the "X00" number generated from the first argument.

    # Argument #3 is an array of subdirectories to be created within this top level directory. The subdirectories within the array are numbered based off the containing directory's prefix.

    def section_assembly(self, directory_level, descriptor, subdirectory_array):
        self.section_name = f'{directory_level}00_{descriptor}' # Create variable of level of directory with description
        self.new_top_level_directory = os.path.join(os.getcwd(), self.section_name) 
        os.mkdir(self.new_top_level_directory)
        print(f'Made directory {self.new_top_level_directory}\n')
        for idx, val in enumerate(subdirectory_array):
            self.current_integer = idx + 1
            self.current_integer = str(self.current_integer)
            self.new_subdirectory_name = f'{directory_level}0{self.current_integer}_{val}'
            print(f'Creating: {self.new_subdirectory_name}')
            self.new_subdirectory_path = os.path.join(self.new_top_level_directory, self.new_subdirectory_name)
            os.mkdir(self.new_subdirectory_path)

    # Read Folder Structure JSON File

    # Reads the JSON file as provided in the PGV class and returns it.

    def read_folder_structure_json_file(self):
        self.json_file = f'{os.path.dirname(os.path.realpath(__file__))}/full_project_structure.json'
        with open(self.json_file, "r") as self.read_file:
            self.data = json.load(self.read_file)

        return self.data

    def local_recursive_subdirectory_creation_loop(self, data, directory):
        self.data = data
        self.directory = directory
        print(f'Total data length is: {len(self.data)}')
        for d in self.data[0]['contents']:
            # print(f'\n\n\n{d}\n\n\n')
            if d['type'] == "directory":
                print(f'\nFound a directory!\n{d["name"]}\n') # Prints 100_level_directories
                self.first_level_path = os.path.join(directory, d['name'])
                print(self.first_level_path)
                try:
                    os.mkdir(self.first_level_path)
                except:
                    pass
                # print(len(d['contents'])) # prints amount of subdirectories
                for c in d['contents']:
                    if c['type'] == "directory":
                        print(f'\n\tSubdirectory name: {c["name"]}\n') # Indents and lists subdirectory names
                        self.second_level_path = os.path.join(self.first_level_path, c['name'])
                        print(f'\t{self.second_level_path}')
                        try:
                            os.mkdir(self.second_level_path)
                        except:
                            pass
                        try:
                            for sd in c['contents']:
                                if sd['type'] == "directory":
                                    self.third_level_path = os.path.join(self.second_level_path, sd['name'])
                                    print(f'\n\t\tSubdirectory name: {sd["name"]}')
                                    print(f'\t\t{self.third_level_path}')
                                    try:
                                        os.mkdir(self.third_level_path)
                                    except:
                                        pass
                                    try:
                                        for sdsd in sd['contents']:
                                            self.fourth_level_path = os.path.join(self.third_level_path, sdsd['name'])
                                            print(f'\n\t\t\tSubdirectory name: {sdsd["name"]}')
                                            print(f'\t\t\t{self.fourth_level_path}')
                                            try:
                                                os.mkdir(self.fourth_level_path)
                                            except:
                                                pass
                                    except:
                                        print("No further subdirectories found.")
                            # print(f'\t\t{len(c["contents"])}')
                        except:
                            print("No further subdirectories found.")
        print("We're done here")

    def copyVideoProject(self):
        self.videoProjectFileDirectory = '600_edit/603_master'
        self.newPath = os.path.join(self.projectPath, self.videoProjectFileDirectory)
        self.remoteProjectFile = f'{Path.home()}/Desktop/gdrive/Clients/ARB/ARB000-templates/001-video-project/XXX123/600_edit/603_master/XXX123.prproj'
        self.newProjFile = os.path.join(self.newPath, f'{self.projectPath.split("/")[-1]}.prproj')
        shutil.copy(self.remoteProjectFile, self.newProjFile)

    def copyAEProject(self):
        self.AEProjectFileDirectory = '700_AE/704_master'
        self.newPath = os.path.join(self.projectPath, self.AEProjectFileDirectory)
        self.remoteProjectFile = f'{Path.home()}/Desktop/gdrive/Clients/ARB/ARB000-templates/001-video-project/XXX123/700_AE/704_master/XXX123.aep'
        self.newProjFile = os.path.join(self.newPath, f'{self.projectPath.split("/")[-1]}.aep')
        shutil.copy(self.remoteProjectFile, self.newProjFile)

    def run(self):
        print('before checker')
        self.check_if_in_project_directory() # Check current working directory to see if basename matches up with AAA123 project code format
        print('after checker')
        self.local_recursive_subdirectory_creation_loop(self.read_folder_structure_json_file(), self.projectPath) # Create all x00 level directories and subdirectories with Section Assembly function
        self.remote_drive_actions()
        self.copyVideoProject()
        self.copyAEProject()
