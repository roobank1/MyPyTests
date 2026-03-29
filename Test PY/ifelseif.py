"""If-Else-If conditional logic and loops to classify ages and numbers."""

age = int(input("Enter your age: "))

if age < 13:
    print("You are a child.")
elif age < 18:
    print("You are a teenager.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are a senior.")

# Loop with if-else-if
print("\nNumbers and their classification:")
for num in range(1, 11):
    if num % 2 == 0 and num % 5 == 0:
        print(f"{num} is even and divisible by 5")
    elif num % 2 == 0:
        print(f"{num} is even")
    elif num % 5 == 0:
        print(f"{num} is divisible by 5")
    else:
        print(f"{num} is odd")