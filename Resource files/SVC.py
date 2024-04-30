from Sampler import Sampler as smp
import numpy as np
import os

os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

from sklearn.utils import shuffle
from keras.models import Sequential
from keras.preprocessing.sequence import pad_sequences
from keras.layers import Conv1D, MaxPool1D, BatchNormalization, Dropout, Masking, SimpleRNN, Dense, Flatten, Bidirectional, LSTM
from keras.optimizers import Adam

path_training   = 'C:\\Users\\ASUS\\Documents\\BME\\6. félév\\Önálló laboratórium\\Signature Verification\\training'
path_testing    = 'C:\\Users\\ASUS\\Documents\\BME\\6. félév\\Önálló laboratórium\\Signature Verification\\testing'
path_evaluation = 'C:\\Users\\ASUS\\Documents\\BME\\6. félév\\Önálló laboratórium\\Signature Verification\\evaluation'


def shuffle_data(X,y):
    return shuffle(X,y, random_state=42)

def load_data(directory):
    Sampler = smp(directory)

    genuine = Sampler.real_signatures
    forged = Sampler.fake_signatures

    X = genuine + forged
    y = [1] * len(genuine) + [0] * len(forged)

    return pad_sequences(X, dtype='float32', padding='post'), np.array(y)

X_train, y_train = load_data(path_training)
X_test, y_test = load_data(path_testing)
X_eval, y_eval = load_data(path_evaluation)

X_train, y_train = shuffle_data(X_train, y_train)
X_test, y_test = shuffle_data(X_test, y_test)
X_eval, y_eval = shuffle_data(X_eval, y_eval)

#define the model
model = Sequential()

model.add(Conv1D(5, kernel_size=20, strides=4, activation='relu', kernel_initializer='he_normal', kernel_regularizer='l2'))
model.add(MaxPool1D(pool_size=4))
model.add(Conv1D(50,kernel_size=10, strides=2, activation='relu'))
model.add(MaxPool1D(pool_size=2))
model.add(Conv1D(25,kernel_size=5, strides=1, activation='relu' ))
model.add(BatchNormalization())
model.add(Dropout(0.5))
model.add(Masking(mask_value=0.0))
model.add(SimpleRNN(10, activation='relu', dropout=0.3))
model.add(Dense(4, activation='sigmoid'))
model.add(Dense(2, activation='softmax'))

#compile the model
optimizer= Adam(learning_rate=0.001)
model.compile(loss='sparse_categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])

#check shuffling of the data
#fit the model
model.fit(X_train, y_train, batch_size=128, epochs=15, validation_data=(X_test, y_test))

#evaluate the model
loss, accuracy = model.evaluate(X_eval, y_eval)

print(f"Test loss: {loss}")
print(f"Test accuracy: {accuracy}")

model.summary()


#shufflnel tuti nem csuszik e  el valami
#model javitasa - oh a cikkel
#parameterek finomhangolasa
