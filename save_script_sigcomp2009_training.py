write_path_testing = "C:\\Users\ASUS\\Documents\\BME\\6. félév\\Önálló laboratórium\\Signature Verification\\testing2\\"
write_path_training = "C:\\Users\ASUS\\Documents\\BME\\6. félév\\Önálló laboratórium\\Signature Verification\\training2\\"
read_path = 'C:\\Users\\ASUS\\Documents\\BME\\6. félév\\Önálló laboratórium\\Signature Verification\\SigComp2009\\Training\\training\\'


for user in range (1, 10, 1):
    for i in range(1, 6, 1):
        file_name = 'NISDCC-' + str(user).zfill(3) + '_' + str(user).zfill(3) + '_' + str(i).zfill(3)

        with open(read_path  + file_name + '.hwr', 'r') as file:
            lines = file.readlines()

        with open(write_path_training + 'U' + str(40 + user) + 'S' + str(i) + '.txt', 'w') as file:
            file.write(''.join(lines))

for user in range (10, 13, 1):
    for i in range(1, 6, 1):
        file_name = 'NISDCC-' + str(user).zfill(3) + '_' + str(user).zfill(3) + '_' + str(i).zfill(3)

        with open(read_path  + file_name + '.hwr', 'r') as file:
            lines = file.readlines()

        with open(write_path_testing + 'U' + str(40 + user) + 'S' + str(i) + '.txt', 'w') as file:
            file.write(''.join(lines))

for user in range(1, 10, 1):
    file_counter = 0
    for forger in range (21, 52, 1):
        if file_counter >= 5:
            break
        for signature in range(1, 6, 1):
            file_name = 'NISDCC-' + str(forger).zfill(3) + '_' + str(user).zfill(3) + '_' +str(signature).zfill(3)

            try:
                with open(read_path + file_name + '.hwr', 'r') as file:
                    lines = file.readlines()
            
                with open(write_path_training +  'U' + str(40 + user) + 'S' + str(20 + signature + forger) + '.txt', 'a') as file:
                    file.write(''.join(lines))
                    file_counter += 1
            except FileNotFoundError:
                print(file_name + ' not found')
                continue
            except Exception as e:
                print(e)
                continue   


for user in range(10, 13, 1):
    file_counter = 0
    for forger in range (21, 52, 1):
        if file_counter >= 5:
            break
        for signature in range(1, 6, 1):
            file_name = 'NISDCC-' + str(forger).zfill(3) + '_' + str(user).zfill(3) + '_' +str(signature).zfill(3)

            try:
                with open(read_path + file_name + '.hwr', 'r') as file:
                    lines = file.readlines()
            
                with open(write_path_testing +  'U' + str(40 + user) + 'S' + str(20 + signature + forger) + '.txt', 'a') as file:
                    file.write(''.join(lines))
                    file_counter += 1
            except FileNotFoundError:
                print(file_name + ' not found')
                continue
            except Exception as e:
                print(e)
                continue
