from MLR import MultivariateLinearRegression

file_name = "winequality.csv"#input("Please enter the name of the CSV File that will act as the data set. Ex: \"Weather.csv\" ")

#var_count = int(input("How many independent variables do you have? "))
independent = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates','alcohol'] #[]
dependent = "quality"#input("What is the name of the dependent variable? Please enter the exact name from the CSV. ")

MLR = MultivariateLinearRegression(file_name, independent, dependent)
MLR.execute()