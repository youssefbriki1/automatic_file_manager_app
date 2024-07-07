import customtkinter as ctk
from MC.model import Model

# Initialize the custom Tkinter environment
ctk.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"



#TODO
# Check llm_sorting_file function and if it could break
# Add folders that user wants to store courses in + description
class App(ctk.CTk):
    def __init__(self, current_directory):
        super().__init__()
        self.title("Custom Tkinter Example")
        self.geometry("1024x1024")
        self.current_directory = current_directory
        self.lobby()
        self.directories = []
        self.files = []
        self.settings = {}
        self.folders_regex = {}
        self.llm_folder = {}

        
        # Button to clear the root window
    
    def lobby(self):
        # Example widgets
        self.clear_root()
        
        self.label = ctk.CTkLabel(self, text="Hello, Welcome to the app!")
        self.label.pack(pady=10)
        
        """
        self.entry = ctk.CTkEntry(self)
        self.entry.pack(pady=10)
        """
        
        self.button = ctk.CTkButton(self, text="Get started", command=self.start_app)
        self.button.pack(pady=10)
        self.button1 = ctk.CTkButton(self, text="Click Me", command=self.report_issue)
        self.button1.pack(pady=10)


        
    def print_entry(self):
        print(self.entry.get())
        
    def start_app(self):
        # Clear the current interface
        self.complete_clear()

        # Add a label for the app page with more padding and a larger font size for prominence
        self.label = ctk.CTkLabel(self, text="This is the app page!", font=("Arial", 16))
        self.label.pack(pady=(20, 10))

        # Create a frame to group the checkboxes for better layout management
        self.checkbox_frame = ctk.CTkFrame(self)
        self.checkbox_frame.pack(pady=10, padx=20, fill="x")

        # Define the state variables for checkboxes
        self.delete_duplicate = ctk.StringVar(value="off")
        self.organize_files = ctk.StringVar(value="off")
        self.organize_files_llm = ctk.StringVar(value="off")
        self.sort_files = ctk.StringVar(value="off")

        # Create and pack checkboxes into the frame with consistent padding
        self.checkbox1 = ctk.CTkCheckBox(
            self.checkbox_frame, text="Delete duplicates",
            variable=self.delete_duplicate, onvalue="on", offvalue="off"
        )
        self.checkbox1.pack(pady=5, anchor="w")  # Align left within the frame

        self.checkbox2 = ctk.CTkCheckBox(
            self.checkbox_frame, text="Organize files",
            variable=self.organize_files, onvalue="on", offvalue="off"
        )
        self.checkbox2.pack(pady=5, anchor="w")

        self.checkbox3 = ctk.CTkCheckBox(
            self.checkbox_frame, text="Use LLM to organize files",
            variable=self.organize_files_llm, onvalue="on", offvalue="off"
        )
        self.checkbox3.pack(pady=5, anchor="w")

        self.checkbox4 = ctk.CTkCheckBox(
            self.checkbox_frame, text="Sort files",
            variable=self.sort_files, onvalue="on", offvalue="off"
        )
        self.checkbox4.pack(pady=5, anchor="w")

        # Add a submit button with more padding and a larger font for prominence
        self.submit_button = ctk.CTkButton(self, text="Submit", command=self.get_dir_or_files, font=("Arial", 14))
        self.submit_button.pack(pady=20)       
        
             


    def complete_clear(self):
        """
        cleans the root and rests the directories and files
        """
        self.clear_root()
        self.directories = []
        self.files = []

    def clear_root(self):
        """
        clears the root
        """
        for widget in self.winfo_children():
            widget.destroy()
        
        
    def add_dir(self):
        """
        allows the user to add a directory
        """
        directory = ctk.filedialog.askdirectory()
        self.directories.append(directory)
        self.get_dir_or_files()
        
        
    def add_files(self):
        """
        allows the user to add files to the list of files
        """
        files = ctk.filedialog.askopenfilenames(initialdir=self.current_directory, filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")])
        self.files.extend([file for file in files])
        self.get_dir_or_files()
            
            
    def get_dir_or_files(self):
        """
        Gets the directories and files that the user wants to add
        """
        
        # Updating the settings dictionary
        self.settings["Duplicates"] = True if self.delete_duplicate.get() == "on" else False
        self.settings["Organize files"] = True if self.organize_files.get() == "on" else False
        self.settings["Organize LLM"] = True if self.organize_files_llm.get() == "on" else False
        self.settings["Sort files"] = True if self.sort_files.get() == "on" else False
        
        print(self.settings)
        self.clear_root()
        self.label = ctk.CTkLabel(self, text="Would you like to add a directory or files?")
        self.label.pack(pady=10)
        self.button = ctk.CTkButton(self, text="Add directory", command=self.add_dir)
        self.button.pack(pady=10)
        self.button = ctk.CTkButton(self, text="Add files", command=self.add_files)
        self.button.pack(pady=10)
        self.label = ctk.CTkLabel(self, text="Directories: " + " - ".join(list(set(self.directories))))
        self.label.pack(pady=10)
        self.label = ctk.CTkLabel(self, text="Files: " + " - ".join(list(set(self.files))))
        self.label.pack(pady=10)
        self.button = ctk.CTkButton(self, text="Next", command=self.options)
        self.button.pack(pady=10)
        self.button = ctk.CTkButton(self, text="Go back", command=self.start_app)
        self.button.pack(pady=10)
        
        
        
    def report_issue(self):
        self.clear_root()
        self.label = ctk.CTkLabel(self, text="Report an issue")
        self.label.pack(pady=10)
        self.entry = ctk.CTkEntry(self)
        self.entry.pack(pady=10)
        self.entry = ctk.CTkEntry(self)
        self.entry.pack(pady=10)
        
        self.button = ctk.CTkButton(self, text="Submit", command=self.submit_issue)
        self.button.pack(pady=10)
        
    def submit_issue(self):
        print("Issue submitted!")
        self.lobby()
        
    def options(self):
        """
        
        """
        if self.files == [] and self.directories == []:
            self.get_dir_or_files()
        self.clear_root()
        
        
        self.label = ctk.CTkLabel(self, text="Options")
        self.label.pack(pady=10)
        
        if self.sort_files.get() == "on":
            self.sorting_options()
        if self.delete_duplicate.get() == "on":
            self.delete_duplicates()
        if self.organize_files.get() == "on":
            self.organize_files()
        
        
        
        self.button = ctk.CTkButton(self, text="Go back", command=self.start_app)
        self.button.pack(pady=10)
        
        
    def frame_helper(self,text:str, options:list=[], has_input:bool=False, fonction=None, is_llm:bool=False):
            
            self.main_frame = ctk.CTkFrame(self)
            self.main_frame.pack()

            self.label = ctk.CTkLabel(self.main_frame, text=text, font=("Arial", 16))
            self.label.pack(pady=(20, 10))

            # Create a sub-frame to hold the radio buttons, centering them within the main frame
            self.radio_frame = ctk.CTkFrame(self.main_frame)
            self.radio_frame.pack()
            # Define options for the radio buttons
            # Create a label
            if has_input:
                label = ctk.CTkLabel(self.radio_frame, text="Enter your text here:")
                label.pack(pady=10)

                # Create a text input field (CTkEntry)
                if is_llm:
                    self.entry1 = ctk.CTkEntry(self.radio_frame, width=200)
                    self.entry1.pack(pady=10)
                else:
                    self.entry2 = ctk.CTkEntry(self.radio_frame, width=200)
                    self.entry2.pack(pady=10)
                

            
                self.button = ctk.CTkButton(self.radio_frame, text="+", command=fonction) # Peut causer des problemes à fix
                self.button.pack(pady=10)
            
            if options:

                # Define a StringVar to hold the selected option
                self.selected_option = ctk.StringVar(value=options[0])

                # Create and place radio buttons into the frame horizontally using pack
                for idx, option in enumerate(options):
                    radio_button = ctk.CTkRadioButton(
                        self.radio_frame, text=option, variable=self.selected_option, value=option
                    )
                    radio_button.pack(side="left", padx=10, pady=5)  # Align horizontally   

    def __llm_sorting_files(self): # Peut causer des problemes
        folder, description = self.entry1.get().split("/")
        self.llm_folder[folder] = description
        print(self.llm_folder)  
        self.sorting_options()
        
    def __regex_sorting_files(self):
        folder, regex = self.entry2.get().split("/")
        self.folders_regex[folder] = regex.split(",")
        print(self.folders_regex)
        self.sorting_options()
        
    def sorting_options(self):
        """
        Where we're going to let the user choose the settings of all the actions they want.
        """
        
        self.clear_root()
        
        if self.settings["Sort files"]:
            text = "Sort files by:"
            options = ["By Name", "By Date", "By Size"]
            self.frame_helper(text=text, options=options)
            
            separator = ctk.CTkFrame(self, height=2, fg_color="gray")
            separator.pack(fill="x", pady=10)


        
        
        if self.settings["Organize files"]:
            
            text = "Put the file in the folder x if if title or content contains regex y, if you wanna add a lot of regex for the same thing, seperate them using commas:"
            self.frame_helper(fonction=self.__regex_sorting_files, text=text, has_input=True, is_llm=False)
            
            self.label = ctk.CTkLabel(self, text="Folders with their regex: " + str(self.folders_regex))       
            self.label.pack(pady=10)

            separator = ctk.CTkFrame(self, height=2, fg_color="gray")
            separator.pack(fill="x", pady=10)
        
            
        
        
        if self.settings["Organize LLM"]:
            text = """What are the the names of the folders you want to store 
            the files in? \n\n 
            ** Write the name of the folder and a description of the folder 
            seperated by a '/' ** \n\n As such: \n\n Calculus/This folder
            contains all the calculus courses"""
            options = ["GPT 3.5", "llama2", "gemma"]
            self.frame_helper(fonction=self.__llm_sorting_files,text=text, options=options, has_input=True,is_llm=True)
            
            
            self.label = ctk.CTkLabel(self, text="Folders with their description: " + str(self.llm_folder))       
            self.label.pack(pady=10)



        # Add a submit button with more padding and centered alignment

        self.submit_button = ctk.CTkButton(self, text="Submit", font=("Arial", 14))
        self.submit_button.pack(pady=20)
        
        
