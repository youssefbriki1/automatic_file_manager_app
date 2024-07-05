import customtkinter as ctk
from MC.model import Model

# Initialize the custom Tkinter environment
ctk.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"



#TODO

# Add folders that user wants to store courses in + description
class App(ctk.CTk):
    def __init__(self, current_directory):
        super().__init__()
        self.title("Custom Tkinter Example")
        self.geometry("1024x768")
        self.current_directory = current_directory
        self.lobby()
        self.directories = []
        self.files = []
        self.settings = {}

        
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
        self.settings["Duplicates"] = self.delete_duplicate.get()
        self.settings["Organize files"] = self.organize_files.get()
        self.settings["Organize LLM"] = self.organize_files_llm.get()
        self.settings["Sort files"] = self.sort_files.get()
        
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
        
    def sorting_options(self):
        """
        Allows the user to select the sorting options
        """
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(expand=True)  # Use pack instead of grid

        # Add a label for the app page with more padding and a larger font size for prominence
        self.label = ctk.CTkLabel(self.main_frame, text="This is the app page!", font=("Arial", 16))
        self.label.pack(pady=(20, 10))

        # Create a sub-frame to hold the radio buttons, centering them within the main frame
        self.radio_frame = ctk.CTkFrame(self.main_frame)
        self.radio_frame.pack()
        # Define options for the radio buttons
        options = ["Delete duplicates", "Organize files", "Use LLM to organize files", "Sort files"]

        # Define a StringVar to hold the selected option
        self.selected_option = ctk.StringVar(value=options[0])

        # Create and place radio buttons into the frame horizontally using pack
        for idx, option in enumerate(options):
            radio_button = ctk.CTkRadioButton(
                self.radio_frame, text=option, variable=self.selected_option, value=option
            )
            radio_button.pack(side="left", padx=10, pady=5)  # Align horizontally

        # Add a submit button with more padding and centered alignment
        self.submit_button = ctk.CTkButton(self.main_frame, text="Submit", font=("Arial", 14))
        self.submit_button.pack(pady=20)
