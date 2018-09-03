import csv
from ast import literal_eval
from itertools import islice

import pandas as pd


def getFieldnames(csvFile):
    """
    Read the first row and store values in a tuple
    """
    with open(csvFile) as csvfile:
        firstRow = csvfile.readlines(1)
        fieldnames = tuple(firstRow[0].strip('\n').split(";"))
    return fieldnames


def writeCursor(csvFile, fieldnames):
    """
    Convert csv rows into an array of dictionaries
    All data types are automatically checked and converted
    """
    cursor = []  # Placeholder for the dictionaries/documents
    with open(csvFile) as csvfile:
        next(csvfile)
        for row in csvfile:
            values = list(row.strip("\n").split(";"))
            for i, value in enumerate(values):
                if i in [1, 7, 8, 9, 10]:
                    nValue = literal_eval(value)
                else:
                    nValue = literal_eval('"'+value+'"')
                values[i] = nValue
            cursor.append(dict(zip(fieldnames, values)))
    return cursor


def get_Models():
    """
    Get the models from the configure_Models.csv
    """
    csv_file = "MachineLearningCSV/_ConfigureNN/configure_Models.csv"
    fieldnames = getFieldnames(csv_file)
    cursor = writeCursor(csv_file, fieldnames)
    return cursor


def get_training_data(training_file):
    dataset = pd.read_csv(training_file, sep=";")
    return dataset


def get_predict_data(predict_file):
    with open(predict_file, "r") as f:
        reader = csv.reader(f, delimiter=";", quoting=csv.QUOTE_NONNUMERIC)
        dataset = list(reader)
        return dataset


def save_predictions(results):
    with open("MachineLearningCSV/_PredictOutput/results.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(results)
