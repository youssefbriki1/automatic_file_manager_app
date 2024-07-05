import ollama
import time
import PyPDF2
import os
import glob
from MC.view import App
from pprint import pp


# Get the directory of the current file

prompt = """You are going to read the following file: 
- If it's related to calculus, output 1
- If it's related to computer architecture, output 2
- If it's related t
"""



if __name__ == "__main__":
    current_directory = os.path.dirname(os.path.abspath(__file__))
    app = App(current_directory)
    app.mainloop() 

path = "/mnt/c/Users/asus/Downloads/"

