from MLR import MultivariateLinearRegression

var_count = int(input("How many independent variables do you have? "))
independent = []

for i in range(len(var_count)):
    value = input("Please input the name of this independent variable: ")
    independent.append(value)

MLR = MultivariateLinearRegression(independent)
MLR.execute()