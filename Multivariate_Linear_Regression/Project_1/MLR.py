import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import os

class MultivariateLinearRegression():
    def __init__(self, file_name, independent, dependent):
        self.directory = os.getcwd() + "/" + file_name
        self.x_name = independent
        self.y_name = dependent
    
    def execute(self):
        print("Hi")