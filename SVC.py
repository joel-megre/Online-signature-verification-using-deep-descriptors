'''
import Sickit
import numpy
import Keras
import Seaborn
import Matplotlib#
'''

import os 
import glob
import pandas as pd
from Signature import Signature as sig

signature = sig()

print(signature.genuineSignatures(5))
print(signature.whichUsersFile('U11S1.TXT'))