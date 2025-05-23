#6
users = [
 {"username": "admin", "role": "superuser"},
 {"username": "john", "role": "user"},
 {"username": "jane", "role": "user"}
]
roles="superuser"
for user in users:
    if user["role"]==roles:
        users.remove(user)
print(users)



#7
scores = []
count = 0
while count < 5:
        score = float(input(f"Enter score (0-100): "))
        if 0 < score < 100:
            scores.append(score)
            count += 1
       
        average = sum(scores) / len(scores)
print(f"Average score: {average:}")



#8
tables = {
 "2x": [],
 "3x": [],
 "4x": []
}    
def mul_table(tables):
    for key in tables:
        mul= int(key.replace("x", ""))
        for i in range(1, 11):
            tables[key].append(mul * i)   
mul_table(tables)
print(tables)



#9
grades = {
    "Class A": [80, 90, 78],
    "Class B": [60, 55, 70],
    "Class C": [88, 92, 85]
}

count = 0

for class_name in grades:
    for grade in grades[class_name]:
        if grade > 75:
            count += 1

print("Number of students who scored more than 75:", count)




