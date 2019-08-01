import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import os

class Linear__Regression():
    
    def __init__(self, file, independent, dependent,):
        self.directory = os.getcwd() + "/" + file
        self.X_name = independent
        self.Y_name = dependent
    
    def read_csv(self):
        self.file_data = pd.read_csv(self.directory)
        #print(self.file_data.describe())

    def variable_reshape(self):
        self.X = self.file_data[self.X_name].values.reshape(-1,1)
        self.Y = self.file_data[self.Y_name].values.reshape(-1,1)

    def set_data(self):
        self.X_train, self.X_test, self.Y_train, self.Y_test = train_test_split(self.X, self.Y, test_size = 0.2, random_state = 0)
    
    def train_model(self):
        self.linear_regressor = LinearRegression()
        self.linear_regressor.fit(self.X_train, self.Y_train)
    
    def test_model(self):
        self.Y_pred = self.linear_regressor.predict(self.X_test)
        self.test_results = pd.DataFrame({"Real Values": self.Y_test.flatten(), "Predicted Values": self.Y_pred.flatten()})
        self.test_results = self.test_results.head(300)
        #print(self.test_results)
    
    def test_model_visualized(self):
        dataframe = self.test_results
        dataframe_list = dataframe.values.tolist()
        #print("Hi")
        
        datapoints = []
        predicted_values = []
        actual_values = []

        for i in range(len(dataframe_list)):
            datapoints.append(i)
            actual_values.append(dataframe_list[i][0])
            predicted_values.append(dataframe_list[i][1])
        
        plt.plot(datapoints, predicted_values, color = "red", linewidth = 1)
        plt.plot(datapoints, actual_values, color = "red", linewidth = 1)
        plt.fill_between(datapoints, predicted_values, actual_values, where= predicted_values > actual_values, facecolor="black")
        plt.fill_between(datapoints, predicted_values, actual_values, where= predicted_values < actual_values, facecolor="black")
        plt.xlabel("Data Points")
        plt.show()
    
    def actual_model_visualized(self):
        plt.scatter(self.X_test, self.Y_test, color = "blue", label = "Data Points")
        plt.plot(self.X_test, self.Y_pred, color = "red", label = "Model Prediction")
        plt.plot(0,0, color = "black", label = self.linear_regressor.score(self.X_test, self.Y_test))
        plt.xlabel(self.X_name)
        plt.ylabel(self.Y_name)
        plt.title(f"Relationship between {self.X_name} and {self.Y_name}")
        plt.legend(loc="lower left")
        plt.show()
    


    def execute(self):
        self.read_csv()
        self.variable_reshape()
        self.set_data()
        self.train_model()
        self.test_model()
        self.test_model_visualized()
        self.actual_model_visualized()
