#!/usr/local/bin/python3

import os
from pathlib import Path

class GlobalVariables():
    def __init__(self):
        pass
        # self.projectDirectory = ''
        # self.homeDirectory = str() # returns user's home directory (ie: /Users/josephdavis)
        
        @property
        def remoteDrivePath(self):
            print(f'{Path.home()}/Desktop/gdrive/Clients')
            # return f'{self.homeDirectory}/Desktop/gdrive/Clients'



# class AeScriptConstants:
#     kbar_icon_path = f'{Global.home}/Development/after-effects/scripts/icons/KBar_Icons.ai'
#     script_directory = f'{Global.home}/Development/after-effects/scripts'

# class ProjectTemplates:
#     video_project_template="/Users/andrewbrady/Desktop/gdrive/Clients/ARB/ARB000-templates/001-video-project/XXX123/600_edit/603_master/XXX123.prproj"
#     ae_project_template="/Users/andrewbrady/Desktop/gdrive/Clients/ARB/ARB000-templates/001-video-project/XXX123/700_AE/704_master/XXX123.aep"

# class ProjectGeneratorVariables:
#     folder_structure_json_file = f'{os.path.dirname(os.path.realpath(__file__))}/folder_structure.json'

# class MostUsedProjectFolders:
#     file_inbox = f'{Global.home}/Desktop/file_inbox'
#     working_music_directory = '400_assets/407_audio/02_MUSIC/01_WORKING'
#     master_music_directory = '400_assets/407_audio/02_MUSIC/02_MASTER'