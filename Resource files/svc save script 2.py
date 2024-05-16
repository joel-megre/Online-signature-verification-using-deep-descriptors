import random

write_path_testing = "C:\\Users\ASUS\\Documents\\BME\\6. félév\\Önálló laboratórium\\Signature Verification\\testing\\"
write_path_training = "C:\\Users\ASUS\\Documents\\BME\\6. félév\\Önálló laboratórium\\Signature Verification\\training\\"
write_path_evaluation = "C:\\Users\ASUS\\Documents\\BME\\6. félév\\Önálló laboratórium\\Signature Verification\\evaluation\\"
read_path = 'C:\\Users\\ASUS\\Documents\\BME\\6. félév\\Önálló laboratórium\\Signature Verification\\SVC 2004\\Task2\\'

for user in range(1, 41, 1):
    genuine_indexes = random.sample(population=range(1,21), k=12)
    forged_indexes = random.sample(population=range(21,41), k=12)
    train_indexes = genuine_indexes + forged_indexes

    test_indexes = list(range(1,41,1))
    for i in train_indexes:
        test_indexes.remove(i)

    eval_indexes = test_indexes.copy()
    genuine_indexes_for_evaluation = random.sample([i for i in eval_indexes if i < 21], k=4)
    forged_indexes_for_evaluation = random.sample([i for i in eval_indexes if i > 20], k=4)
    eval_indexes = genuine_indexes_for_evaluation + forged_indexes_for_evaluation
    for i in eval_indexes:
        test_indexes.remove(i)

    for i in train_indexes:
        file_name = 'U' + str(user) + 'S' + str(i)

        with open(read_path + file_name + '.TXT', 'r') as file:
            lines = file.readlines()

        modified_lines = []
        for line_num, line in enumerate(lines):
            fields = line.split()
            if line_num != 0:
                fields[2], fields[6] = fields[6], fields[2]
                fields = [field for j, field in enumerate(fields) if j not in [3, 6]]
            modified_line = ' '.join(fields)
            modified_lines.append(modified_line)

        with open(write_path_training + file_name + '.txt', 'a') as file:
            file.write('\n'.join(modified_lines))

    for i in test_indexes:
        file_name = 'U' + str(user) + 'S' + str(i)

        with open(read_path + file_name + '.TXT', 'r') as file:
            lines = file.readlines()

        modified_lines = []
        for line_num, line in enumerate(lines):
            fields = line.split()
            if line_num != 0:
                fields[2], fields[6] = fields[6], fields[2]
                fields = [field for j, field in enumerate(fields) if j not in [3,6]]
            modified_line = ' '.join(fields)
            modified_lines.append(modified_line)

        with open(write_path_testing + file_name + '.txt', 'a') as file:
            file.write('\n'.join(modified_lines))

    for i in eval_indexes:
        file_name = 'U' + str(user) + 'S' + str(i)

        with open(read_path + file_name + '.TXT', 'r') as file:
            lines = file.readlines()

        modified_lines = []
        for line_num, line in enumerate(lines):
            fields = line.split()
            if line_num != 0:
                fields[2], fields[6] = fields[6], fields[2]
                fields = [field for j, field in enumerate(fields) if j not in [3,6]]
            modified_line = ' '.join(fields)
            modified_lines.append(modified_line)

        with open(write_path_evaluation + file_name + '.txt', 'a') as file:
            file.write('\n'.join(modified_lines))
