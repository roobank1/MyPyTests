# Program to check if a sub-list with sum equal to zero exists

numbers = [4, 2, -3, 1, 6]                      # Example list

for i in range(len(numbers)):                   # Select starting position of sub-list
    total = 0                                   # Start sum as 0
    
    for j in range(i, len(numbers)):            # Expand the sub-list
        total += numbers[j]                     # Add next element to the sum
        if total == 0:                          # Check if sum becomes zero
            
            print("Sub-list with sum 0 exists") 
            
            break                              # Stop if a sub-list with sum zero is found