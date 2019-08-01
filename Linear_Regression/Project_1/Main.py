from Linear_Regression import Linear__Regression

FILE_NAME = input("Please input the CSV File that contains your DataSet. Ex: \"Weather.csv\" ")
X = input("What is the independent variable? ")
Y = input("What is the dependent variable? ")

Regression = Linear__Regression(FILE_NAME, X, Y)
Regression.execute()
