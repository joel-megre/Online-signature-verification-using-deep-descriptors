import os
import pandas as pd

class SVC2004:
    def __init__(self, userId, directory):
        self.userId = userId
        self.directory = directory
        self.signatures = self.loadSignatures()

    def loadSignatures(self):
        signatures = {}

        for filename in os.listdir(self.directory):
            if filename.endswith(".TXT"):
                with open(os.path.join(self.directory, filename), 'r') as file:
                    numPoints = int(file.readline().strip())
                    df = pd.read_csv(file, sep = ' ', names=['X', 'Y', 'Tstamp', 'Bstatus', 'AzAngle', 'AltAngle', 'Pressure'])
                    signatures[filename] = df
        return signatures
    
    def normalize(self):
        for filename, df in self.signatures.items():
            # Normalize alignment - align to start at point 0 
            # .min() returns with the lowest value
            # kell a tobbi ertek is? (szoveg szerint minden erteket normalizalunk)
            df['X'] -= df['X'].min()
            df['Y'] -= df['Y'].min()

            # Normalize size - make every signature the same size
            # eleg ez vagy (df['X'] - df['X'].max()) / (df['X'].min() - df['X'].max())?
            df['x'] /= df['X'].max()
            df['Y'] /= df['Y'].max()

            self.signatures[filename] = df 




