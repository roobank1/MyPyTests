#Separates a list of numbers into even and odd numbers
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

even_numbers = []                                   # An empty list to store even numbers
odd_numbers = []                                    # An empty list to store odd numbers

for num in numbers:                                 # Loop to check if the number is divisible by 2
    if num % 2 == 0:
        even_numbers.append(num)                    # If remainder is 0, it is an even number
    else:
        odd_numbers.append(num)                     # If remainder is not 0, it is an odd number

print("Even Numbers:", even_numbers)                # Print all even numbers
print("Odd Numbers:", odd_numbers)                  # Print all odd numbers
