#1
students = [
    {"name": "Alice", "marks": [80, 85, 90]},
    {"name": "Bob", "marks": [70, 75, 68]},
    {"name": "Charlie", "marks": [90, 92, 88]}
]
def students_average(students):
    
    for student in students:
        avg = sum(student["marks"]) / len(student["marks"])
        student["average"] = avg
        print(f"{student['name']}: Average = {student['average']:}")

students_average(students)


#2
attendance = {
 "Alice": [1, 1, 0, 1, 1],
 "Bob": [0, 1, 0, 0, 1],
 "Charlie": [1, 1, 1, 1, 1]
}
remove_items=[]
for item in attendance:
    key = item
    value = attendance[item]
    count=0
    for v in value:
        if v==1:
            count+=1
    if count < 3:
           remove_items.append(key)
for i in remove_items:
     attendance.pop(i)
print(attendance)



#3
messages = [
 {"user": "alice", "msg": "Hi"},
 {"user": "bob", "msg": "Hello"},
 {"user": "charlie", "msg": "Hey"},
 {"user": "dave", "msg": "Yo"}
]
messages.reverse()
items=0
while items<2:
     items+=1
     messages.pop()
print(messages)


#4
products = [
 {"name": "Laptop", "price": 60000},
 {"name": "Mouse", "price": 500},
 {"name": "Phone", "price": 25000}
]
for product in products:
    price= product["price"]
    if price>10000:
        print("expensive")
    else:
        print("budget")




#5
catalog = [
 {"id": 1, "name": "TV"},
 {"id": 2, "name": "Fridge"},
 {"id": 3, "name": "Microwave"}
]
product="TV"
for products in catalog:
    if products["name"]==product:
        catalog.remove(products)
print(catalog)








