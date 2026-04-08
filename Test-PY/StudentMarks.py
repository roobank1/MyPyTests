"""Manages student data in a dictionary - finding toppers, adding, and removing students."""
students = { 
            "Student1": ["Arul", 89], 
            "Student2": ["Abdul", 96], 
            "Student3": ["Anbu", 77], 
            "Student4": ["Anu", 25], 
            "Student5": ["Asha", 54] 
          }

print("Printing all students data:")
for roll, details in students.items():
    print(roll, ":", details[0], "-", details[1])

topper = max(students, key=lambda x: students[x][1])
print("\nTopper:", topper, "-", students[topper])

special = min(students, key=lambda x: students[x][1])

students["Student6"] = ["Arun", 95]
print("\nAfter Adding New Student:")
print(students)

students.pop(special)
print("\nAfter Removing Student with lowest marks:")
print(students)