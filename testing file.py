def getid(filename):
    parts = filename.split('_')

    user_id = parts[0].split('-')[1]
    return user_id

filename = "NISDCC-001-001_001"

user_id = getid(filename)
print(user_id)