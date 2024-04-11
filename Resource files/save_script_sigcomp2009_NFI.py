import random
import os

write_path_testing = "C:\\Users\ASUS\\Documents\\BME\\6. félév\\Önálló laboratórium\\Signature Verification\\testing\\"
write_path_training = "C:\\Users\ASUS\\Documents\\BME\\6. félév\\Önálló laboratórium\\Signature Verification\\training\\"
write_path_evaluation = "C:\\Users\ASUS\\Documents\\BME\\6. félév\\Önálló laboratórium\\Signature Verification\\evaluation\\"

read_path_genuine = 'C:\\Users\\ASUS\\Documents\\BME\\6. félév\\Önálló laboratórium\\Signature Verification\\SigComp2009\\NFI_\\genuines\\'
read_path_forgery = 'C:\\Users\\ASUS\\Documents\\BME\\6. félév\\Önálló laboratórium\\Signature Verification\\SigComp2009\\NFI_\\forgeries\\'

users_for_testing_and_training = [3,4,6,9,11,13,14,16,17,22,23,27,28,32,39,41,42,43,49,51,52,54,56]
users_for_eval = [59,60,61,74,77,80,85,88,89,100]

files = [f for f in os.listdir(read_path_forgery)]
for user in users_for_testing_and_training:

    users_for_testing_forgery = [f for f in  files if f.startswith('NFI-'+ str(user).zfill(3))]

    selected_files = random.sample(users_for_testing_forgery, 6)

    for signature in selected_files:
        try:
            sig_id = signature[-8:-4]
            with open(read_path_forgery + signature, 'r') as file:
                lines = file.readlines()

            with open(write_path_testing + 'U' + str(46 + user) + 'S' + sig_id + '.txt', 'a') as file:
                file.write(''.join(lines))
        except FileNotFoundError:
            print(signature + ' not found')
            continue
        except Exception as e:
            print(e)
            continue

    users_for_training_forgery = [f for f in users_for_testing_forgery if f not in selected_files]

    selected_files_for_training = random.sample(users_for_training_forgery, 6)

    for signature in selected_files_for_training:
        try:
            sig_id = signature[-8:-4]
            with open(read_path_forgery + signature, 'r') as file:
                lines = file.readlines()

            with open(write_path_training + 'U' + str(43 + user) + 'S' + sig_id + '.txt', 'a') as file:
                file.write(''.join(lines))
        except FileNotFoundError:
            print(signature + ' not found')
            continue
        except Exception as e:
            print(e)
            continue

    users_for_testing = random.sample(population = range(1, 12), k = 6) #might be subject to change 
    users_for_training = list(range(1, 13, 1))

    for i in users_for_testing:
        users_for_training.remove(i)

    for i in users_for_testing:
        file_name = 'NFI-' + str(user).zfill(3) + str(i).zfill(2) + str(user).zfill(3)

        try:
            with open(read_path_genuine + file_name + '.hwr', 'r') as file:
                lines = file.readlines()

            with open(write_path_testing + 'U' + str(46 + user) + 'S' + str(i) + '.txt', 'a') as file:
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
            with open(read_path_genuine + file_name + '.hwr', 'r') as file:
                lines = file.readlines()

            with open(write_path_training + 'U' + str(43 + user) + 'S' + str(i) + '.txt', 'a') as file:
                file.write(''.join(lines))
        except FileNotFoundError:
            print(file_name + ' not found')
            continue
        except Exception as e:
            print(e)
            continue


for user in users_for_eval:
    #users_for_evaluation = random.sample(population = range(1, 12), k = 12) #could be more based on genuines
    users_for_evaluation = list(range(1, 13, 1))
    for i in users_for_evaluation:
        file_name = 'NFI-' + str(user).zfill(3) + str(i).zfill(2) + str(user).zfill(3)

        try:
            with open(read_path_genuine + file_name + '.hwr', 'r') as file:
                lines = file.readlines()

            with open(write_path_evaluation + 'U' + str(40 + user) + 'S' + str(i) + '.txt', 'a') as file:
                file.write(''.join(lines))
        except FileNotFoundError:
            print(file_name + ' not found')
            continue
        except Exception as e:
            print(e)
            continue
            
    users_for_testing_forgery = [f for f in  files if f.startswith('NFI-'+ str(user).zfill(3))]

    selected_files = random.sample(users_for_testing_forgery, 12)

    for signature in selected_files:
        try:
            sig_id = signature[-8:-4]
            with open(read_path_forgery + signature, 'r') as file:
                lines = file.readlines()

            with open(write_path_evaluation + 'U' + str(40 + user) + 'S' + sig_id + '.txt', 'a') as file:
                file.write(''.join(lines))
        except FileNotFoundError:
            print(signature + ' not found')
            continue
        except Exception as e:
            print(e)
            continue