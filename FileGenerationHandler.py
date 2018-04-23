import os

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
