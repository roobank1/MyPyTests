# name = input("Enter your name :")
# print("Hai", name)

# age = int(input("Enter your age :"))

# if age >=18:
#     print("You are eligible to vote")
# else:   
#     print("You are not eligible to vote")



numbers = [2,6,4,5,7,9,2, 1,3,4, 8]

def add(num):
	return num + num
list2 = []
for num in numbers:
	list2.append(add(num))
print(list2)
