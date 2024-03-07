import pandas as pd
import os
import glob


class Signature:
    def __init__(self):
        self.Path = 'C:\\Users\\ASUS\\Documents\\BME\\6. félév\\Önálló laboratórium\\Signature Verification\\SVC 2004\\Task2'
        self.dir =os.listdir(self.Path)
        self.allData = pd.DataFrame()
        self.allFiles = os.path.join(self.Path + "/*.TXT")
        self.li = []
        
    def readFolderData(self):
        for filename in self.allFiles:
            df = pd.read_csv(filename, sep=' ', header=0)
            self.li.append(df)
        self.allData = pd.concat(self.li, axis=0, ignore_index=True)
        return self.allData

    def genuinityCheck(self, signatureId):
        if 1 <= signatureId <= 20:
            return 'Genuine'
        else:
            return 'Forged'

    def genuineSignatures(self, userId):
        genuineSignatures = []

        for filename in self.dir:
            if filename.endswith(".TXT"):
                tempUser, signatureId = map(int, filename[1:-4].split('S'))
                if tempUser == userId and self.genuinityCheck(signatureId) == 'Genuine':
                    genuineSignatures.append(filename)
        return genuineSignatures

    def forgedSignatures(self, userId):
        forgedSignatures = []

        for filename in self.dir:
            if filename.endswith(".TXT"):
                tempUser, signatureId = map(int, filename[1:-4].split('S'))
                if tempUser == userId and self.genuinityCheck(signatureId) == 'Forged':
                    forgedSignatures.append(filename)
        return forgedSignatures
    

    def whichUsersFile(self, textfile):
        for filename in self.dir:
            if filename.endswith(".TXT"):
                if(textfile == filename):
                    return filename[1:3].split('S')

    def getFolderData(self):
        return self.allData
