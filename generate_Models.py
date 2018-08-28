from keras.layers import Activation, Dense, Layer
<<<<<<< HEAD
from keras.metrics import (mean_absolute_error, mean_absolute_percentage_error,
                           mean_squared_error, mean_squared_logarithmic_error)
from keras.models import Sequential


def create_model(arr, hidden_activation='relu', output_activation='linear', loss_f='mean_squared_error', optimizer_f='Adamax', metrics_f='accuracy'):
    """
    Create a Squential Model (Keras)
        :param arr: List of the nodes of the hidden layers
        :param hidden_activation: Activation function for all the hidden layers. Default = 'Relu'
        :param output_activation: Activation function for the output layer. Default = 'linear'
        :param loss_f: Loss function for the Model. Default = 'mean_squared_error' 
        :param optimizer_f: Optimizer for the model. Default = 'Adamax'
        :param metrics_f:  Metric for the model. Default = 'accuracy'
    """
=======
from keras.models import Sequential
from keras.metrics import mean_absolute_error, mean_absolute_percentage_error, mean_squared_error, mean_squared_logarithmic_error


def create_model(arr, hidden_activation='relu', output_activation='linear', loss_f='mean_squared_error', optimizer_f='Adamax', metrics_f='accracy'):
>>>>>>> 48c000c... Update - Dict for created Models
    model = Sequential()
    for i in range(len(arr)):
        if i != 0 and i != len(arr)-1:
            if i == 1:
                model.add(Dense(arr[i], input_dim=arr[0],
                                activation=hidden_activation))
            else:
                model.add(Dense(arr[i], activation=hidden_activation))
    model.add(Dense(arr[-1], activation=output_activation))
    model.compile(loss=loss_f, optimizer=optimizer_f, metrics=[metrics_f])
    return model
