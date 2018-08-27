import csv

def get_Models():
    models = []
    file = csv.DictReader(open("MachineLearningCSV/_ConfigureNN/configure_Models.csv", "r+"), dialect="excel")
    for row in file:
        models.append(row)
    return models