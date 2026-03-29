# Create a list of squares of even numbers from a given list using lambda and list comprehension

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]                # List of numbers to process

is_even = lambda x: x % 2 == 0                    # Lambda function to check if number is even
squares = [x**2 for x in numbers if is_even(x)]   # List comprehension to create a list of squares of even numbers using the lambda function

print(squares)