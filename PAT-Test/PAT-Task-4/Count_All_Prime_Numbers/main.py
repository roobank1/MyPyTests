#Count the list of all Prime numbers
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

prime_numbers = []                              # An empty list to store prime numbers

for num in numbers:                             # Loop through each number in the list
    for i in range(2, num):                     # Check divisibility from 2 up to num - 1
        if num % i == 0:                        # If divisible, not prime
            break                     
        else:                                   # If no divisors found, it's prime
            prime_numbers.append(num)           # Add number if prime

prime_count = len(prime_numbers)                # Count total prime numbers found

print("Prime Numbers:", prime_numbers)          # Print all prime numbers
print("Total Prime Numbers:", prime_count)      # Print the total count
