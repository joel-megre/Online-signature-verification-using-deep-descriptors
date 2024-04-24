import os
import pandas as pd

class Signature:
    def __init__(self, userId, directory):
        self.userId = userId
        self.directory = directory
        self.signatures = self.load_and_normalize()

    def load_and_normalize(self):
        signatures = {}

        for filename in os.listdir(self.directory):
            if filename.startswith(f"U{self.userId}S") and filename.endswith(".txt"):
                with open(os.path.join(self.directory, filename), 'r') as file:
                    df = pd.read_csv(file, sep = ' ', names=['X', 'Y', 'AZ', 'AL', 'P'], skiprows=1)

                    df = df - df.iloc[0]

                    df = (df - df.max()) / (df.min() - df.max())

                    signature_id = int(filename.split('S')[1].split('.')[0])

                    label = 1 if signature_id <= 20 else 0

                    signatures[filename] = (df,label)
        return signatures
    
    def get_signatures(self, signature_id):
        filename = f"U{self.userId}S{signature_id}.txt"

        return self.signatures[filename]
    
    def get_all_signatures(self):
        return self.signatures




