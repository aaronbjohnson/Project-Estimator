from sklearn.preprocessing import LabelEncoder
import os

def remove_column(dataset, column):
    """
    This will delete a column from a dataset.
    Column needs to be a string
    """
    del dataset[column]
    return

def label_encode(dataset, column):
    """
    This will encode a binary categorical variable.
    Column needs to be a string
    """
    labelencoder_X = LabelEncoder()
    dataset[column] = labelencoder_X.fit_transform(dataset[column])
    return
