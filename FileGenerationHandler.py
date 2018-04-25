import os
import datetime

class FileGenerationHandler():

    def __init__(self, rootDir):

        self.rootDir = rootDir
        self.fileTreeIsComplete = "File tree is not complete. Click Generate to complete."
        self.count = 0

        self.semesters = ["Semester 1", "Semester 2"]
        self.units = ["Unit 1", "Unit 2", "Unit 3", "Unit 4", "Unit 5",
                    "Unit 6", "Unit 7", "Unit 8", "Unit 9"]
        self.subUnitFolders = ["Assignments", "Documents", "Lessons"]

    def doInEachSubFolder(self, commandToDo):

        # Calls a function given the path argument, for each folder in the directory
        for i in range(len(self.semesters)):

            for x in range(len(self.units)):

                for j in range(len(self.subUnitFolders)):

                    path = os.path.join(self.rootDir, self.semesters[i], self.units[x], self.subUnitFolders[j])

                    commandToDo(path)

    def genDir(self, path):
        # Create directory in given path if it does not already exist
        if not os.path.exists(path):
            os.makedirs(path)

    def increaseFolderCount(self, path):
        # Increases the count for each folder in the directory,
        # Count will be 54 if the directory is completely generated
        if os.path.exists(path):
            self.count += 1

    def generateFileTree(self):
        self.doInEachSubFolder(self.genDir)

    def isCompletelyGenerated(self):

        self.count = 0
        # Count increased in this method
        self.doInEachSubFolder(self.increaseFolderCount)

        if self.count != 54:
            self.fileTreeIsComplete = "File tree is not complete. Click Generate to complete."
        else:
            self.fileTreeIsComplete = "File tree has been generated"

        return self.fileTreeIsComplete

    def generatePMR(self):
        # Will generate a PMR outline in each project folder within any of the subdirectories
        self.doInEachSubFolder(self.findProjFolder)

    # Defines a general PMR outline with automatic title and date generation
    def pmrOutline(self, folder):
        now = datetime.datetime.now()
        date = str(now.month) + "/" + str(now.day) + "/" + str(now.year)
        return ("Project Title: " + folder + "\nPurpose: \nName: \nDate: " + date + "\n\n" +
                "**************************** P M R ***********************************\n\n" +
                "<+s> \n\n<-s> \n\n*********************************************************************")

    def findProjFolder(self, path):
        for folder in os.listdir(path):
            foundPMR = False
            # Do nothing with files, only want folders
            if not '.' in folder:
                # Get each file in each folder
                for file in os.listdir(os.path.join(path, folder)):
                    if file == 'PMR.txt':
                        foundPMR = True
                        break
                if foundPMR:
                    # Do not change anything if project already contains a PMR
                    print "Found pmr in " + os.path.join(path, folder)
                else:
                    print "PMR not found in " + os.path.join(path, folder) + ". Generating now"
                    # Generate pmr in project directories where it does not yet exist under the name PMR.txt
                    with open(os.path.join(path, folder, "PMR.txt"), "w+") as pmr:
                        pmr.write(self.pmrOutline(folder))
