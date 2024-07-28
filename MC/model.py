import time
import PyPDF2
import os
import glob
from pprint import pp
import automatic_file_manager as afm


class Model:
    def __init__(self, settings, files=[], directories=[]) -> None:
        self.files = files
        self.directories = directories
        self.settings = settings
        self.FilesManager = afm.FilesManager()
        self.settings_map_function = {"Duplicates": self.FilesManager.remove_duplicates,
                                      "Organize files": self.FilesManager.organize_files,
                                      "Organize LLM": self.FilesManager.organize_llm,            
        }
    
    def run(self):
        for setting, value in self.settings.items():
            if value:
                self.settings_map_function[setting]()
                print(f"Setting {setting} has been applied")
        print("All settings have been applied")
