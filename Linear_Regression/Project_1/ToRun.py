from Main import LinearRegression

FILE_NAME = input("Please input the CSV File that contains your DataSet. Ex: \"Weather.csv\" ")

Regression = LinearRegression(FILE_NAME)
Regression.execute()
