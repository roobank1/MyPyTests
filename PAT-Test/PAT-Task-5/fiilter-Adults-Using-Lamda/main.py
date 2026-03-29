# Filter list of people with their names and ages using lamda function

people = [                                                   # List of dictionaries representing people with their names and ages
    {"name": "Arjun", "age": 17},
    {"name": "Aprita", "age": 21},
    {"name": "Aravind", "age": 16},
    {"name": "Arun", "age": 25},
    {"name": "Ambru", "age": 20},
    {"name": "Arul", "age": 15},
    {"name": "Anu", "age": 19}
]                                                               

adults = filter(lambda person: person["age"] >= 18, people)  # Filter people who are 18 or older

names = list(map(lambda person: person["name"], adults))     # Map the remaining people to their names

print("Adults:", names)