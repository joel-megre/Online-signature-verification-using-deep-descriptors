from Sampler import Sampler as smp
import matplotlib.pyplot as plt
import numpy as np
import os

os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'


from keras.utils import to_categorical
from keras.models import Sequential
from keras.preprocessing.sequence import pad_sequences
from keras.layers import Conv1D, MaxPool1D, BatchNormalization, Dropout, Masking, SimpleRNN, Dense, ZeroPadding1D
from keras.optimizers import Adam
from keras.regularizers import l2
from keras.callbacks import ReduceLROnPlateau

path_training   = 'C:\\Users\\ASUS\\Documents\\BME\\6. félév\\Önálló laboratórium\\Signature Verification\\training'
path_testing    = 'C:\\Users\\ASUS\\Documents\\BME\\6. félév\\Önálló laboratórium\\Signature Verification\\testing'
path_evaluation = 'C:\\Users\\ASUS\\Documents\\BME\\6. félév\\Önálló laboratórium\\Signature Verification\\evaluation'


training = smp(path_training)
testing = smp(path_testing)
evaluation = smp(path_evaluation)

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

#print(X_train.shape)

#define the model
model = Sequential()

model.add(Conv1D(100, kernel_size=20, strides=4, activation='relu', kernel_initializer='he_normal', kernel_regularizer=(l2(0.01))))
model.add(MaxPool1D(pool_size=4))
model.add(Conv1D(50,kernel_size=10, strides=2, activation='relu'))
model.add(MaxPool1D(pool_size=2))
model.add(Conv1D(25,kernel_size=5, strides=1, activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(0.5))
model.add(Masking(mask_value=0.0))
model.add(SimpleRNN(10, activation='relu', dropout=0.3))
model.add(Dense(4, activation='sigmoid'))
model.add(Dense(2, activation='softmax'))

#compile the model
optimizer= Adam(learning_rate=0.01)
model.compile(loss='sparse_categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])

#fit the model
model.fit(X_train, y_train, batch_size=64, epochs=50, validation_data=(X_test, y_test),  shuffle=True)

#evaluate the model
loss, accuracy = model.evaluate(X_eval, y_eval)

print(f"Test loss: {loss}")
print(f"Test accuracy: {accuracy}")

#model.summary()