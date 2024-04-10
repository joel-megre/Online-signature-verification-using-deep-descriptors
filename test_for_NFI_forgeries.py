import os

read_path = 'C:\\Users\\ASUS\\Documents\\BME\\6. félév\\Önálló laboratórium\\Signature Verification\\SigComp2009\\NFI_\\forgeries\\'


last_three = set()

for filename in os.listdir(read_path):
    last_threechars = filename[-7:-3]
    last_three.add(last_threechars)

result = list(last_three)
result.sort()
print(result)
