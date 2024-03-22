from sig2class import Signature
import os

class Sampler:
    def __init__(self, directory):
        self.directory = directory
        self.database = self.load_database()

    #key = userId, values = dictionary of signatures
    def load_database(self):
        database = {}

        user_ids = {filename[1] for filename in os.listdir(self.directory) if filename.startswith("U") and filename.endswith(".txt")}

        for user_id in user_ids:
            user = Signature(user_id, self.directory)
            database[user_id] = user.signatures

        return database