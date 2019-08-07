import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import os
import matplotlib.pyplot as plt

class Linear__Regression():
    def __init__(self, file, independent, dependent,):
        self.directory = os.getcwd() + "/" + file # Get the file directory
        self.X_name = independent # Variable Name
        self.Y_name = dependent # Variable Name
        self.continue_predicting = False
    
    def read_csv(self):
        self.file_data = pd.read_csv(self.directory) # In a [[Variable1], [Variable2]] format. Regressor takes [[Variable1, Variable2], [Variable1, Variable2]] format
        self.file_data.isnull().any
        self.file_data = self.file_data.fillna(method='ffill')
        #print(self.file_data.describe())

    def variable_reshape(self):
        self.X = self.file_data[self.X_name].values.reshape(-1,1) # This command turns everything into something like a feature vector so that the weights can be assigned
        self.Y = self.file_data[self.Y_name].values.reshape(-1,1) # To return back to its normal form, do .flatten()
        

    def set_data(self):
        self.X_train, self.X_test, self.Y_train, self.Y_test = train_test_split(self.X, self.Y, test_size = 0.25, random_state = 0)
    
    def train_model(self):
        self.linear_regressor = LinearRegression() # Loading pre-built & optimized regressor model 
        self.linear_regressor.fit(self.X_train, self.Y_train) # Training the model on the specified data set
    
    def test_model(self):
        self.Y_pred = self.linear_regressor.predict(self.X_test)
        self.test_results = pd.DataFrame({"Real Values": self.Y_test.flatten(), "Predicted Values": self.Y_pred.flatten()})
        self.test_results = self.test_results.head(200) # This is for visualization, you will visualize some of the data to see the accuracy
        #print(self.test_results)
    
    def prepare_visualization(self):
        dataframe = self.test_results
        dataframe_list = dataframe.values.tolist() # Converting back to List format because MatPlotLib takes lists.
        
        self.datapoints = []
        self.predicted_values = []
        self.actual_values = []

        for i in range(len(dataframe_list)):
            self.datapoints.append(i)
            self.actual_values.append(dataframe_list[i][0])
            self.predicted_values.append(dataframe_list[i][1])
    
    def visualize_error(self):
        plt.plot(self.datapoints, self.predicted_values, color = "red", linewidth = 1)
        plt.plot(self.datapoints, self.actual_values, color = "red", linewidth = 1)
        plt.fill_between(self.datapoints, self.predicted_values, self.actual_values, where= self.predicted_values > self.actual_values, facecolor="black")
        plt.fill_between(self.datapoints, self.predicted_values, self.actual_values, where= self.predicted_values < self.actual_values, facecolor="black")
        plt.xlabel("Data Points")
        plt.show()
    
    def visualize_model(self):
        fig = plt.figure()
        ax1 = fig.add_subplot(211)
        ax1.scatter(self.X_test, self.Y_test, color = "blue", label = "Data Points")
        ax1.plot(self.X_test, self.Y_pred, color = "red", label = "Model Prediction")
        ax1.plot(0,0, color = "black", label = self.linear_regressor.score(self.X_test, self.Y_test))
        ax1.set_xlabel(self.X_name)
        ax1.set_ylabel(self.Y_name)
        ax1.set_title(f"Relationship between {self.X_name} and {self.Y_name}")
        ax1.legend(loc="upper left")

        ax2 = fig.add_subplot(212)
        ax2.plot(self.datapoints, self.predicted_values, color = "red", linewidth = 0.5, label = "Predicted Values. Black filling is error")
        ax2.plot(self.datapoints, self.actual_values, color = "blue", linewidth = 0.5, label = "Actual Values")
        ax2.fill_between(self.datapoints, self.predicted_values, self.actual_values, where= self.predicted_values > self.actual_values, facecolor="black")
        ax2.fill_between(self.datapoints, self.predicted_values, self.actual_values, where= self.predicted_values < self.actual_values, facecolor="black")
        ax2.set_xlabel("Data Points")
        ax2.set_ylabel("Values")
        ax2.set_title(f"Relationship between the Predicted and Actual Values to display Error")
        ax2.legend(loc="upper left")
        plt.tight_layout(pad=0.5)
        plt.show()

        '''
        plt.scatter(self.X_test, self.Y_test, color = "blue", label = "Data Points")
        plt.plot(self.X_test, self.Y_pred, color = "red", label = "Model Prediction")
        plt.plot(0,0, color = "black", label = self.linear_regressor.score(self.X_test, self.Y_test))
        plt.xlabel(self.X_name)
        plt.ylabel(self.Y_name)
        plt.title(f"Relationship between {self.X_name} and {self.Y_name}")
        plt.legend(loc="upper left")
        plt.show()
        '''
    
    def execute(self):
        self.read_csv()
        self.variable_reshape()
        self.set_data()
        self.train_model()
        self.test_model()
        self.prepare_visualization()
        #self.visualize_error()
        self.visualize_model()