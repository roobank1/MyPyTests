# Lambda function to check if a string is a number
 
is_number = lambda s: s.isdigit()           # Lambda function that returns True if the string consists of digits only, indicating it's a number

user_input = input("Enter a string: ")      # Get input from the user 
 
if is_number(user_input):                   # Check if the input is a number
    print("YES, this string is a number")
else:
    print("NO, this string is NOT a number")