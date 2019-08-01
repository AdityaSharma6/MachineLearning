import pandas as pd 
import numpy as np
import os

class LinearRegression():
    
    def __init__(self, file):
        self.directory = os.getcwd() + "/" + file
    
    def execute(self):
        print(self.directory)


#file_name = pd.read_csv("Weather.csv")