#matplotlib - drawing of the signatures
'''
fig, ax = plt.subplots()

ax.plot(first[0]['X'], first[0]['Y'])

ax.set(xlabel='X')
ax.set(ylabel='Y')

plt.show()

'''

import matplotlib.pyplot as plt

import matplotlib.pyplot as plt

# Step 3: Load the data with row skip
x = []
y = []
row_skip = 1  # Adjust this value according to the number of rows you want to skip
with open('C:\\Users\\ASUS\\Documents\\BME\\6. félév\\Önálló laboratórium\\Signature Verification\\training\\U41S46.txt', 'r') as file:
    for i, line in enumerate(file):
        if i < row_skip:
            continue  # Skip the rows
        data = line.split()  # Assuming space-separated data
        x.append(float(data[0]))  # Assuming x values are in the first column
        y.append(float(data[1]))  # Assuming y values are in the second column

# Step 4: Plot the data
plt.plot(x, y)
plt.xlabel('X Axis Label')
plt.ylabel('Y Axis Label')
plt.title('Your Title Here')
plt.grid(True)
plt.show()
'''
training = smp(path_training)
testing = smp(path_testing)
evaluation = smp(path_evaluation)
#shuffle the data
#get all genuine and forged signatures
genuine_training = training.real_signatures
forged_training =  training.fake_signatures

genuine_testing = testing.real_signatures
forged_testing =  testing.fake_signatures

genuine_evaluation =  evaluation.real_signatures
forged_evaluation =  evaluation.fake_signatures

#combine genuine and forged signatures and create labels
X_train = genuine_training + forged_training
y_train = [1] * len(genuine_training) + [0] * len(forged_training)

X_test = genuine_testing + forged_testing
y_test = [1] * len(genuine_testing) + [0] * len(forged_testing)

X_eval = genuine_evaluation + forged_evaluation
y_eval = [1] * len(genuine_evaluation) + [0] * len(forged_evaluation)


#convert to numpy arrays
X_train = pad_sequences(X_train, dtype='float32', padding='post')
y_train = np.array(y_train)

X_test = pad_sequences(X_test, dtype='float32', padding='post')
y_test = np.array(y_test)

X_eval = pad_sequences(X_eval, dtype='float32', padding='post')
y_eval = np.array(y_eval)

X_train, y_train = shuffle(X_train, y_train)
X_test, y_test = shuffle(X_test, y_test)
X_eval, y_eval = shuffle(X_eval, y_eval)
'''