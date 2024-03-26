import random

write_path_testing = "C:\\Users\ASUS\\Documents\\BME\\6. félév\\Önálló laboratórium\\Signature Verification\\testing2\\"
write_path_training = "C:\\Users\ASUS\\Documents\\BME\\6. félév\\Önálló laboratórium\\Signature Verification\\training2\\"
read_path = 'C:\\Users\\ASUS\\Documents\\BME\\6. félév\\Önálló laboratórium\\Signature Verification\\SigComp2009\\Training\\training\\'

for user in range(21, 52, 1):
    #genuine_user_indexes = random.sample(population= range(1, 12), k =5)
    #forged_user_indexes = random.sample(population=range(21, 51), k=5)
    #train_indexes = genuine_user_indexes + forged_user_indexes
    #test_indexes = list(range(1, 51, 1))
    train_indexes = random.sample(population=range(1, 12), k=5)
    test_indexes = list(range(1, 12, 1))

    for i in train_indexes:
        test_indexes.remove(i)

    for i in train_indexes:
        random_signature = random.randint(1, 5)
 
        file_name = 'NISDCC-' + str(user).zfill(3) + '_' + str(i).zfill(3) + '_' + str(random_signature).zfill(3)

        with open(read_path  + file_name + '.hwr', 'r') as file:
            lines = file.readlines()

        # 'U'+ user_id + 'S' + signature_id
        with open(write_path_training + 'U' + str(40 + i) + 'S' + str(20 + i) + '.txt', 'w') as file:
        #with open(write_path_training + file_name + '.txt', 'w') as file:
            file.write(''.join(lines))
