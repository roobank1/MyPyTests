# Program to find the triplet in a list whose sum equals the given value

numbers = [10, 20, 30, 9]                                                     # Sample list of integers
target = 59                                                                   # Target value we want the sum to match

n = len(numbers)                                                              # Find the length of the list

for i in range(n):                                                            # First loop selects first element of the triplet
    for j in range(i + 1, n):                                                 # Second loop selects second element
        for k in range(j + 1, n):                                             # Third loop selects third element
            if numbers[i] + numbers[j] + numbers[k] == target:                # Check if the sum equals 59
                
                print("Triplet found:", numbers[i], numbers[j], numbers[k])   # Print the matching triplet