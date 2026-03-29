# Program to find the first non-repeating element in a list

numbers = [4, 5, 1, 2, 0, 4, 5, 2 , 10, 11, 13 , 10 ]  # List of integers given by the user

for num in numbers:                                    # Loop through each number in the list
    
    if numbers.count(num) == 1:                        # Check if the number appears only once in the list
        print("First non-repeating element:", num)     # Print the first non-repeating element
        break                                          # Stop the loop once the first unique element is found