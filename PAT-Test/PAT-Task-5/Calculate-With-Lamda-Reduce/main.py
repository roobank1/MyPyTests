# Calculate the product of all numbers in a list using lambda and reduce

from functools import reduce                      # Import reduce function

numbers = [2, 3, 4, 5, 6]                         # List of numbers to multiply
product = reduce(lambda x, y: x * y, numbers)     # Use reduce and lambda to multiply all numbers

print("Product of all numbers:", product)