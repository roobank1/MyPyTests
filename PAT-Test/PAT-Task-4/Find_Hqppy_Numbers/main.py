# Given list
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

happy_numbers = []                                # An emptyist to store happy numbers

for num in numbers:                               # Loop through each number
    n = num                                       # Copy original number

    for _ in range(n):                          
        total = 0                                 # Reset sum

        for digit in str(n):                      # Go through each digit
            total += int(digit) * int(digit)      # Add square of digit

        n = total                                 # Update number

        if n == 1:                                # If it becomes 1
            happy_numbers.append(num)             # It is a happy number
            break                                 # Stop checking this number

print("Happy Numbers:", happy_numbers)
print("Total Happy Numbers:", len(happy_numbers))
