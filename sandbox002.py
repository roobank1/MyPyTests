
file = open("numbers.txt", "w")
file.write(" 1 \n 2 \n 3 \n 4 \n 5 \n")
file.close()          


                         

file = open("numbers.txt", "r")                 
numbers = []

for line in file:
    if line != "\n":  
        numbers.append(int(line)) 



def add_numbers(num_list):
    total = 0
    
    for num in num_list:
        total = total + num 
    
    return total 
result = add_numbers(numbers) 
print("Sum of numbers:", result)