import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import os

class MultivariateLinearRegression():

    def __init__(self, file, independent, dependent):
        self.directory = "/Users/adityasharma/Desktop/SoftwareEngineering/Files/MachineLearning/Multivariate_Linear_Regression/Project_1/" + file
        self.X_name = independent
        self.Y_name = dependent

        #self.x_values = self.data[independent].values
        #self.y_values = self.data[dependent].values
    
    def read_csv(self):
        self.data = pd.read_csv(self.directory)
        self.data.isnull().any
        self.data = self.data.fillna(method='ffill')
    
    def variable_reshape(self):
        self.X = self.data[self.X_name].values
        self.Y = self.data[self.Y_name].values
        #print(self.X)
        #print(self.Y)

    def set_data(self):
        self.X_train, self.X_test, self.Y_train, self.Y_test = train_test_split(self.X, self.Y, test_size = 0.2, random_state = 0)
    
    def train_model(self):
        self.MLR = LinearRegression()
        self.model = self.MLR.fit(self.X_train, self.Y_train)
        coefficient = pd.DataFrame(self.MLR.coef_, self.X_name)
        print(coefficient)

        
    
    def test_model(self):
        self.predictions = self.MLR.predict(self.X_test)
        self.prediction_df = pd.DataFrame({"Actual Values": self.Y_test, "Predicted Values": self.predictions})
        self.prediction_df = self.prediction_df.head(200)
    
    def prepare_visualization(self):
        dataframe = self.prediction_df
        dataframe_list = dataframe.values.tolist()

        self.datapoints = []
        self.predicted_values = []
        self.actual_values = []

        for i in range(len(dataframe_list)):
            self.datapoints.append(i)
            self.actual_values.append(dataframe_list[i][0])
            self.predicted_values.append(dataframe_list[i][1])
    
    def visualize_model(self):
        #print(self.X_test)
        #fig = plt.figure()
        '''
        ax1 = fig.add_subplot(211)
        ax1.scatter(self.X_test, self.Y_test, color = "blue", label = "Data Points")
        ax1.plot(self.X_test, self.predictions, color = "red", label = "Model Prediction")
        ax1.plot(0,0, color = "black", label = self.MLR.score(self.X_test, self.Y_test))
        ax1.set_xlabel(self.X_name)
        ax1.set_ylabel(self.Y_name)
        ax1.set_title(f"Relationship between {self.X_name} and {self.Y_name}")
        ax1.legend(loc="upper left")'''

        print('Mean Absolute Error:', metrics.mean_absolute_error(self.Y_test, self.predictions))  
        print('Mean Squared Error:', metrics.mean_squared_error(self.Y_test, self.predictions))  
        print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(self.Y_test, self.predictions)))
        
        #ax1 = fig.add_subplot(211)
        plt.plot(0,0, color = "black", label = self.MLR.score(self.X_test, self.Y_test))
        plt.plot(self.datapoints, self.predicted_values, color = "red", linewidth = 0.5, label = "Predicted Values.")
        plt.plot(self.datapoints, self.actual_values, color = "blue", linewidth = 0.5, label = "Actual Values")
        plt.fill_between(self.datapoints, self.predicted_values, self.actual_values, where= self.predicted_values > self.actual_values, facecolor="black", label = "Error")
        plt.fill_between(self.datapoints, self.predicted_values, self.actual_values, where= self.predicted_values < self.actual_values, facecolor="black")
        plt.xlabel("Data Points")
        plt.ylabel("Values")
        plt.title(f"Relationship between the Predicted and Actual Values to display Error")
        plt.legend(loc="upper left")
        plt.tight_layout(pad=0.5)
        plt.show()
        

    def execute(self):
        self.read_csv()
        self.variable_reshape()
        self.set_data()
        self.train_model()
        self.test_model()
        self.prepare_visualization()
        self.visualize_model()



