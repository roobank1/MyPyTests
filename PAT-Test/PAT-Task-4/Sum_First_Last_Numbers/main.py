# Program to find the sum of the first and last digit of an integer

num = int(input("Enter an integer more than three digit: "))    # Take an integer input from the user

last_digit = num % 10                                           # Get the last digit by finding the remainder when divided by 10
first_digit = num                                               # Copy the number to another variable to find the first digit
  
while first_digit >= 10:                                        # Loop until the number becomes a single digit
    first_digit = first_digit // 10                             # Remove the last digit by performing integer division by 10
    
sum_digits = first_digit + last_digit                           # Calculate the sum of the first and last digit

print("First digit:", first_digit)                              # Print the first digit
print("Last digit:", last_digit)                                # Print the last digit
print("Sum of first and last digit:", sum_digits)               # Print the sum of the first and last digit
