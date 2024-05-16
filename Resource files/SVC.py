from Sampler import Sampler as smp
import numpy as np
import os

os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

from sklearn.utils import shuffle
from keras.models import Sequential
from keras.preprocessing.sequence import pad_sequences
from keras.layers import Conv1D, MaxPool1D,  Dropout, Masking, SimpleRNN, Dense, BatchNormalization,Input
from keras.initializers import he_normal
from keras.regularizers import l2
from keras.optimizers import Adam

path_training   = 'C:\\Users\\ASUS\\Documents\\BME\\6. félév\\Önálló laboratórium\\Signature Verification\\training'
path_testing    = 'C:\\Users\\ASUS\\Documents\\BME\\6. félév\\Önálló laboratórium\\Signature Verification\\testing'
path_evaluation = 'C:\\Users\\ASUS\\Documents\\BME\\6. félév\\Önálló laboratórium\\Signature Verification\\evaluation'

def load_data(directory):
    Sampler = smp(directory)

    genuine = Sampler.real_signatures
    forged = Sampler.fake_signatures

    X = genuine + forged
    y = [1] * len(genuine) + [0] * len(forged)

    X,y = shuffle(X,y, random_state=42)

    return pad_sequences(X, dtype='float32', padding='post'), np.array(y)

X_train, y_train = load_data(path_training)
X_test, y_test = load_data(path_testing)
X_eval, y_eval = load_data(path_evaluation)

#define the model
model = Sequential()
model.add(Input(shape=(None, 5)))
model.add(Conv1D(5, kernel_size=20, strides=4, activation='relu', kernel_initializer=he_normal(), kernel_regularizer=l2()))
model.add(MaxPool1D(pool_size=4))
model.add(Conv1D(50, kernel_size=10, strides=2, activation='relu'))
model.add(MaxPool1D(pool_size=2))
model.add(Conv1D(25,kernel_size=5, strides=1, activation='relu' ))
model.add(BatchNormalization())
model.add(Dropout(0.5))
model.add(Masking(mask_value=0.0))
model.add(SimpleRNN(20, activation='relu', dropout=0.3))
model.add(Dense(4, activation='sigmoid'))
model.add(Dense(1, activation='sigmoid'))

#compile the model
optimizer= Adam(learning_rate=0.001)
model.compile(loss='binary_crossentropy', optimizer=optimizer, metrics=['accuracy'])

#fit the model
model.fit(X_train, y_train, batch_size=32, epochs=100, validation_data=(X_test,y_test))

#evaluate the model
loss, accuracy = model.evaluate(X_test,y_test)
print(f"Test loss: {loss}")
print(f"Test accuracy: {accuracy}")

loss_eval, accuracy_eval = model.evaluate(X_eval, y_eval)

print(f"Evaluation loss: {loss_eval}")
print(f"Evaluation accuracy: {accuracy_eval}")

#save the model
model.save('C:\\Users\\ASUS\\Documents\\BME\\6. félév\\Önálló laboratórium\\Signature Verification\\saved_model\\model5.keras')

from keras.models import load_model
new_model = load_model('C:\\Users\\ASUS\\Documents\\BME\\6. félév\\Önálló laboratórium\\Signature Verification\\saved_model\\85_9.keras')

loss_loaded, accuracy_loaded = new_model.evaluate(X_test, y_test)


print(f"Loaded model loss: {loss_loaded}")
print(f"Loaded model accuracy: {accuracy_loaded}")
#model.summary()