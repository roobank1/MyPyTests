# Program to find duplicate elements present in three lists

list1 = [1, 2, 3, 4, 5, 6]                                   # First list 
list2 = [4, 5, 6, 7, 8, 9]                                   # Second list 
list3 = [0, 2, 4, 6, 8, 10]                                  # Third list 

duplicates = []                                              # An empty list to store duplicate elements

for num in list1:                                            # Loop through each element in the first list
    
    if num in list2 and num in list3:                        # Check if the element exists in both list2 and list3
        
        duplicates.append(num)                               # Add the element to duplicates list

print("Duplicate elements in all three lists:", duplicates)  # Print the duplicate elements found in all three lists