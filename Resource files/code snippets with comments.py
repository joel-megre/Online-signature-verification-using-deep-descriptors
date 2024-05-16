#matplotlib - drawing of the signatures
import pandas as pd
import matplotlib.pyplot as plt

path  = 'C:\\Users\\ASUS\\Documents\\BME\\6. félév\\Önálló laboratórium\\Signature Verification\\training2\\NFI-00309003.txt'

data = pd.read_csv(path, skiprows=1, delim_whitespace=True, header=None, usecols=[0,1])

# Plot the contents of the file
plt.figure(figsize=(10, 6))

# Assuming you want to plot all columns against the first one
plt.plot(data[0], data[1], label='Signature')

plt.legend()
plt.show()



# import matplotlib.pyplot as plt

# import matplotlib.pyplot as plt

# # Step 3: Load the data with row skip
# x = []
# y = []
# row_skip = 1  # Adjust this value according to the number of rows you want to skip
# with open('C:\\Users\\ASUS\\Documents\\BME\\6. félév\\Önálló laboratórium\\Signature Verification\\training\\U41S46.txt', 'r') as file:
#     for i, line in enumerate(file):
#         if i < row_skip:
#             continue  # Skip the rows
#         data = line.split()  # Assuming space-separated data
#         x.append(float(data[0]))  # Assuming x values are in the first column
#         y.append(float(data[1]))  # Assuming y values are in the second column

# # Step 4: Plot the data
# plt.plot(x, y)
# plt.xlabel('X Axis Label')
# plt.ylabel('Y Axis Label')
# plt.title('Your Title Here')
# plt.grid(True)
# plt.show()
# '''
# training = smp(path_training)
# testing = smp(path_testing)
# evaluation = smp(path_evaluation)
# #shuffle the data
# #get all genuine and forged signatures
# genuine_training = training.real_signatures
# forged_training =  training.fake_signatures

# genuine_testing = testing.real_signatures
# forged_testing =  testing.fake_signatures

# genuine_evaluation =  evaluation.real_signatures
# forged_evaluation =  evaluation.fake_signatures

# #combine genuine and forged signatures and create labels
# X_train = genuine_training + forged_training
# y_train = [1] * len(genuine_training) + [0] * len(forged_training)

# X_test = genuine_testing + forged_testing
# y_test = [1] * len(genuine_testing) + [0] * len(forged_testing)

# X_eval = genuine_evaluation + forged_evaluation
# y_eval = [1] * len(genuine_evaluation) + [0] * len(forged_evaluation)


# #convert to numpy arrays
# X_train = pad_sequences(X_train, dtype='float32', padding='post')
# y_train = np.array(y_train)

# X_test = pad_sequences(X_test, dtype='float32', padding='post')
# y_test = np.array(y_test)

# X_eval = pad_sequences(X_eval, dtype='float32', padding='post')
# y_eval = np.array(y_eval)

# X_train, y_train = shuffle(X_train, y_train)
# X_test, y_test = shuffle(X_test, y_test)
# X_eval, y_eval = shuffle(X_eval, y_eval)
# '''

# from keras.models import load_model
# new_model = load_model('C:\\Users\\ASUS\\Documents\\BME\\6. félév\\Önálló laboratórium\\Signature Verification\\saved_model\\model2.h5')

# loss_loaded, accuracy_loaded = new_model.evaluate(X_test, y_test)


# print(f"Loaded model loss: {loss_loaded}")
# print(f"Loaded model accuracy: {accuracy_loaded}")

