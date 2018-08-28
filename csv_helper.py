import csv
from itertools import islice
from ast import literal_eval

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
                if i in [1,7,8,9]:
                    nValue = literal_eval(value)
                else:
                    nValue = literal_eval('"'+value+'"')
                values[i] = nValue
            cursor.append(dict(zip(fieldnames, values)))
    return cursor

def get_Models():
    models = []
    csv_file = "MachineLearningCSV/_ConfigureNN/configure_Models.csv"
    fieldnames = getFieldnames(csv_file)
    cursor = writeCursor(csv_file, fieldnames)
    return cursor