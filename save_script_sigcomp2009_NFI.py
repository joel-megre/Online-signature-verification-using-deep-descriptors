import random

write_path_testing = "C:\\Users\ASUS\\Documents\\BME\\6. félév\\Önálló laboratórium\\Signature Verification\\testing3\\"
write_path_training = "C:\\Users\ASUS\\Documents\\BME\\6. félév\\Önálló laboratórium\\Signature Verification\\training3\\"
write_path_evaluation = "C:\\Users\ASUS\\Documents\\BME\\6. félév\\Önálló laboratórium\\Signature Verification\\evaluation3\\"
read_path = 'C:\\Users\\ASUS\\Documents\\BME\\6. félév\\Önálló laboratórium\\Signature Verification\\SigComp2009\\NFI_\\genuines\\'

for user in range (1, 71, 1):
    users_for_testing = random.sample(population = range(1, 12), k = 6) #might be subject to change 
    users_for_training = list(range(1, 13, 1))

    for i in users_for_testing:
        users_for_training.remove(i)

    for i in users_for_testing:
        file_name = 'NFI-' + str(user).zfill(3) + str(i).zfill(2) + str(user).zfill(3)

        try:
            with open(read_path + file_name + '.hwr', 'r') as file:
                lines = file.readlines()

            with open(write_path_testing + 'U' + str(53 + user) + 'S' + str(i) + '.txt', 'w') as file:
                file.write(''.join(lines))
        except FileNotFoundError:
            print(file_name + ' not found')
            continue
        except Exception as e:
            print(e)
            continue

    for i in users_for_training:
        file_name = 'NFI-' + str(user).zfill(3) + str(i).zfill(2) + str(user).zfill(3)

        try:
            with open(read_path + file_name + '.hwr', 'r') as file:
                lines = file.readlines()

            with open(write_path_training + 'U' + str(49 + user) + 'S' + str(i) + '.txt', 'w') as file:
                file.write(''.join(lines))
        except FileNotFoundError:
            print(file_name + ' not found')
            continue
        except Exception as e:
            print(e)
            continue

for user in range(71, 101, 1):
    users_for_evaluation = random.sample(population = range(1, 12), k = 6) #could be more based on genuines

    for i in users_for_evaluation:
        file_name = 'NFI-' + str(user).zfill(3) + str(i).zfill(2) + str(user).zfill(3)

        try:
            with open(read_path + file_name + '.hwr', 'r') as file:
                lines = file.readlines()

            with open(write_path_evaluation + 'U' + str(40 + user) + 'S' + str(i) + '.txt', 'w') as file:
                file.write(''.join(lines))
        except FileNotFoundError:
            print(file_name + ' not found')
            continue
        except Exception as e:
            print(e)
            continue
