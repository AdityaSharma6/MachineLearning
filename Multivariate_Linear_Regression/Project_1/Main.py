from MLR import MultivariateLinearRegression

file_name = input("Please enter the name of the CSV File that will act as the data set. Ex: \"Weather.csv\" ")

var_count = int(input("How many independent variables do you have? "))
independent = []

for i in range(len(var_count)):
    variable = input(f"Please enter the name of variable number {i}. It should be exactly how it is written in the CSV file. Same as title.")
    independent.append(variable)


#independent = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates','alcohol'] #[]
dependent = input("What is the name of the dependent variable? Please enter the exact name from the CSV. ") #"quality"

MLR = MultivariateLinearRegression(file_name, independent, dependent)
MLR.execute()