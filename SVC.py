'''
import Sickit
import os
import numpy
import Keras
import Seaborn
import Matplotlib#
'''

import ast

svcValues = []
#read multiple open('C:\\path1','C:\\path2','C:\\path3')
#how to store values?

with open('C:\\Users\\ASUS\\Documents\\BME\\6. félév\\Önálló laboratórium\\Signature Verification\\SVC 2004\\Task2\\U1S1.TXT') as f:
    next(f)
    for line in f:
        values = line.strip().split(' ')
        for value in values:
            svcValues.append(ast.literal_eval(value))

print(svcValues)

f.close()

