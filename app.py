from Tkinter import *
from tkFileDialog import *
from FileGenerationHandler import *

class App(Frame):

    def __init__(self, root=None):

        self.currentDirectory = "None"
        self.browseWidgets = []
        self.mainWidgets = []

        # Initialize file generation class
        self.fileGenerationHandler = FileGenerationHandler(self.currentDirectory)

        # Initialize frame
        Frame.__init__(self, root)
        self.root = root
        self.setupGeometry(500, 300)

        # First create main group of widgets and immediately hide them to show initial screen
        self.createMainWidgets()
        self.hideWidgets(self.mainWidgets)
        self.createBrowseWidgets()

        self.pack()

    def setupGeometry(self, w, h):
        self.WIDTH = w
        self.HEIGHT = h
        # Screen dimensions
        screenWidth = self.root.winfo_screenwidth()
        screenHeight = self.root.winfo_screenheight()

        # Center position on the screen
        self.XPOS = (screenWidth / 2) - (self.WIDTH / 2)
        # YPOS is 10% of screenHeight higher (it looks a little better)
        self.YPOS = (screenHeight / 2) - (self.HEIGHT / 2) - (screenHeight / 10)
        self.root.geometry('%dx%d+%d+%d' % (self.WIDTH, self.HEIGHT, self.XPOS, self.YPOS))

    def createBrowseWidgets(self):

        self.button = Button(self, text="Browse New Directory", command=self.browseDirectory)
        self.button.grid(row=0, column=0, pady=10)

        self.currentDirectoryText = Label(self, text="Current Directory:\n" + self.currentDirectory, bg="white")
        self.currentDirectoryText.grid(row=1, column=0, pady=10)

        self.continueButton = Button(self, text="Continue With Current Directory", command=self.useDirectory)
        self.continueButton.grid(row=2, column=0, pady=10)

        self.errorText = Label(self, text="You must select a directory to use.", fg="red")

        # Add all to browse widgets group
        self.browseWidgets.append(self.button)
        self.browseWidgets.append(self.currentDirectoryText)
        self.browseWidgets.append(self.continueButton)
        self.browseWidgets.append(self.errorText)

        menu = Menu(self.root)
        subMenu = Menu(menu, tearoff=0)
        menu.add_cascade(label="Edit", menu=subMenu)
        subMenu.add_command(label="Change Directory", command=self.browseDirectory)
        self.root.config(menu=menu)

    def createMainWidgets(self):

        self.currentDirText = Label(self, text="Current Directory: " + self.currentDirectory, bg="white")
        self.currentDirText.grid(row=0, column=0, padx=5)

        self.changeDirButton = Button(self, text="Change", command=self.browseDirectory)
        self.changeDirButton.grid(row=0, column=1)

        self.generateFileTreeButton = Button(self, text="Generate File Tree", command=self.generateStatus)
        self.generateFileTreeButton.grid(row=1, column=0, columnspan=2, pady = 5)

        self.fileTreeIsCompleteText = Label(self, text=self.fileGenerationHandler.fileTreeIsComplete)
        self.fileTreeIsCompleteText.grid(row=2, column=0, columnspan=2, pady=5)

        # Add all to main widget group
        self.mainWidgets.append(self.currentDirText)
        self.mainWidgets.append(self.changeDirButton)
        self.mainWidgets.append(self.generateFileTreeButton)
        self.mainWidgets.append(self.fileTreeIsCompleteText)

    def browseDirectory(self):

        self.currentDirectory = askdirectory() #tkFileDialog
        # Updating text info
        self.currentDirectoryText["text"] = "Current Directory:\n" + self.currentDirectory
        self.currentDirText["text"] = "Current Directory: " + self.currentDirectory
        self.fileGenerationHandler.rootDir = self.currentDirectory

        self.fileTreeIsCompleteText["text"] = self.fileGenerationHandler.isCompletelyGenerated()

        # Do not show error if a directory has been selected
        if (self.currentDirectory != "None"):
            self.errorText["text"] = ""

        # Display None instead of nothing when no dir selected
        if (self.currentDirectory == ""):
            self.currentDirectory = "None"
            self.currentDirectoryText["text"] = "Current Directory:\n" + self.currentDirectory
            self.currentDirText["text"] = "Current Directory: " + self.currentDirectory

    # Display error message, do not leave screen until a directory has been selected
    def useDirectory(self):
        if (self.currentDirectory == "None"):
            # Display error message if no directory is selected
            self.errorText.grid(row=3, column=0)
            self.errorText["text"] = "You must select a directory to use."
        else:
            # Display different set of widgets
            self.hideWidgets(self.browseWidgets)
            self.showWidgets(self.mainWidgets)

    def showWidgets(self, widgets):
        for widget in widgets:
            widget.grid()

    def hideWidgets(self, widgets):
        for widget in widgets:
            # widget.grid() will replace it back to its original position
            widget.grid_remove()

    # Use generate method from file generation handler and display the text to the screen
    def generateStatus(self):
        self.fileTreeIsCompleteText["text"] = self.fileGenerationHandler.generateFileTree()
        self.fileTreeIsCompleteText["text"] = self.fileGenerationHandler.isCompletelyGenerated()

root = Tk()
app = App(root)
app.mainloop()
