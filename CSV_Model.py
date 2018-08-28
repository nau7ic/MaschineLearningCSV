import csv
import glob
import os

import numpy as np
import pandas as pd
from keras.models import Sequential
from sklearn.model_selection import train_test_split

import csv_helper
from generate_Models import create_model
<<<<<<< HEAD

# Configuration
training_data_path = 'MachineLearningCSV/_TrainingData/'
predict_data_path = 'MachineLearningCSV/_PredictData/'

# Get Models from CSV
models_data = csv_helper.get_Models()

# Dict for storing the Models
models = {}

# Add the generated Models to the Dict
for i in models_data:
    key = i["Name"]
    models[key] = create_model(i["Layer_Nodes"], i["Hidden_Activation"],
                               i["Output_Activation"], i["Loss"], i["Optimizer"], i["Metrics"])

# Get the training data
for filename in glob.glob(os.path.join(training_data_path, '*.csv')):
    dataset = csv_helper.get_training_data(filename)

# Get the predict data
for filename in glob.glob(os.path.join(predict_data_path, '*.csv')):
    predict_dataset = csv_helper.get_predict_data(filename)

# Split the data to X and Y
trainX = dataset[dataset.columns.difference([dataset.columns[-1]])]
trainY = dataset[dataset.columns[-1]]

# Fit every model in die dict
for model_name, model in models.items():
    n = 0
    model.fit(np.array(trainX), np.array(trainY),
              epochs=models_data[n]["Epochs"], verbose=models_data[n]["Verbose"])
    if models_data[n]["Save"] == 1:
        model.save_weights(
            'MachineLearningCSV/_ModelWeights/{}_weights.h5'.format(model_name), overwrite=False)
    n = + 1


results = []
# Prediction with every model in the dict
for model_name, model in models.items():
    for row in predict_dataset:
        data = np.array([row])
        results.append(model.predict(data))

csv_helper.save_predictions(results)

print("Fertig!")
=======

models_data = csv_helper.get_Models()

models = {}

for i in models_data:
    key = i["Name"]
    models[key] = create_model(i["Layer_Nodes"], i["Hidden_Activation"],
                               i["Output_Activation"], i["Loss"], i["Optimizer"], i["Metrics"])

print(models)

# model.fit(np.array(trainX),np.array(trainY),epochs=20,callbacks=[plot_losses], verbose)
>>>>>>> 48c000c... Update - Dict for created Models
