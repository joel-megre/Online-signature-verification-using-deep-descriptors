from Signature import Signature
import os

class Sampler:
    def __init__(self, directory):
        self.directory = directory
        self.real_signatures = []
        self.fake_signatures = []
        self.database = self.load_database()

    #key = userId, values = dictionary of signatures
    def load_database(self):
        database = {}

        user_ids = {filename[1:filename.index('S')] for filename in os.listdir(self.directory) if filename.startswith("U") and filename.endswith(".txt")}

        for user_id in user_ids:
            user = Signature(user_id, self.directory)
            database[user_id] = user.signatures

            for signature in user.signatures.values():
                data, label = signature
                if label == 1:
                    self.real_signatures.append(data)
                else:
                    self.fake_signatures.append(data)
                    
        return database