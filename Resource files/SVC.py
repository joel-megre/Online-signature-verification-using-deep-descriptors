from Signature import Signature as svc
from Sampler import Sampler as smp
from keras.models import Sequential
from keras.layers import Conv1D, MaxPool1D, BatchNormalization, Dropout, Masking, SimpleRNN, Dense

path_training = 'C:\\Users\\ASUS\\Documents\\BME\\6. félév\\Önálló laboratórium\\Signature Verification\\training'
path_testing = 'C:\\Users\\ASUS\\Documents\\BME\\6. félév\\Önálló laboratórium\\Signature Verification\\testing'
path_evaluation = 'C:\\Users\\ASUS\\Documents\\BME\\6. félév\\Önálló laboratórium\\Signature Verification\\evaluation'

first_user = svc(1,  path_training)
sampler = smp(path_training)

first_signature = first_user.get_signatures(1)
first = sampler.database['1']['U1S1.txt']
print(first)

#model
model = Sequential()

#filters-t mire kell állítani?
model.add(Conv1D(filters=None, kernel_size=20, strides=4, activation='relu', kernel_initializer='he_normal', kernel_regularizer='l2'))
model.add(MaxPool1D(pool_size=8))
model.add(Conv1D(filters=None,kernel_size=2, strides=2, activation='relu'))
model.add(MaxPool1D(pool_size=4))
model.add(Conv1D(filters=None,kernel_size=5, strides=1, activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(0.5))
model.add(Masking(mask_value=0.0))
model.add(SimpleRNN(10, activation='relu', dropout=0.3))
model.add(Dense(4, activation='sigmoid'))
model.add(Dense(2, activation='softmax'))

#loss and optimizer (model compilation?)

#training (epochs, batchsize)

#evaluation