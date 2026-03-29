# Print the Fibonacci series up to n terms using a lambda function and reduce

from functools import reduce                                                            # Import reduce function from functools
fibonacci = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n-2), [0, 1])      # Lambda function to generate Fibonacci series

n = 15                                                                                  # Number of terms in the Fibonacci series to generate
result = fibonacci(n)                                                                   # Call the lambda function to get the Fibonacci series up to n terms

print("Fibonacci series up to", n, "terms:", result)