from sklearn.metrics import confusion_matrix
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_confusion_matrix(y_test, y_pred, model_name):
    '''
    Function to easily draw the confusion matrix and see the results of the model evaluation.
    - y_test: real results
    - y_pred: predicted results
    - model_name: name of the model for the plot
    '''

    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(6, 5))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=["Class 0", "Class 1"], yticklabels=["Clase 0", "Clase 1"])
    plt.xlabel('Predict')
    plt.ylabel('Real')
    plt.title(f'Confusion Matrix - {model_name}')
    plt.show()