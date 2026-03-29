# Extract year, month, and day from a datetime object using a lambda function

from datetime import datetime

date = datetime(2025, 11, 28)                         # Create a datetime object
get_date_parts = lambda d: (d.year, d.month, d.day)   # Lambda function to extract year, month, and day from the datetime object
year, month, day = get_date_parts(date)               # Use the lambda function and extract the results into year, month, and day variables

print("Year:", year)
print("Month:", month)
print("Day:", day)