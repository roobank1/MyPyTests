# Program to find the minimum element in a rotated and sorted list

numbers = [4, 5, 6, 7, 1, 2, 3, 9, 10, 11, 12]        # Sample rotated and sorted list
min_element = numbers[0]                            

for num in numbers:                                   # Loop through each element in the list    
    if num < min_element:                             # Check if the current element is smaller than the stored minimum        
        min_element = num                             # Update the minimum value if a smaller element is found

print("Minimum element in the list : ", min_element)  # Print the minimum element