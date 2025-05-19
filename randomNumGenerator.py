# 4.7 Project: Random Number Generator

# Importing random module
import random

# Generating random number and assigning it to a variable
random_number = random.randint(1, 100)

# Printing random_number and its data type
print("Number is", random_number)
print("Data type is", type(random_number))

# Multi word variables
camelCaseVariable = "camelCase"
PascalCaseVariable = "PascalCase"
snake_case_variable = "snake_case"

# Converting random_number to a float
float_random_number = float(random_number)
complex_random_number = complex(random_number)

print("Number after converting to a float is", float_random_number)
print("Data type is", type(float_random_number))

print("Number after converting to a complex is", complex_random_number)
print("Data type is", type(complex_random_number))