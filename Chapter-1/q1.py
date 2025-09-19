# Take two numbers as input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Calculate results
_sum = num1 + num2
_difference = num1 - num2
_product = num1 * num2

# Handle division carefully (avoid division by zero)
if num2 != 0:
    _quotient = num1 / num2
else:
    _quotient = "Undefined (division by zero)"

# Print the results
print(f"Sum: {_sum}")
print(f"Difference: {_difference}")
print(f"Product: {_product}")
print(f"Quotient: {_quotient}")
