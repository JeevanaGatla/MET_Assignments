#Assign_1
numbers = [34, 35, 84, 23, 19]
numbers.sort()               
numbers.remove(23)           
print(numbers)

#Assign_2
todo_list = ["wake up", "Exercise", "work"]
del todo_list[2]              
todo_list.pop(1)              
todo_list.remove("wake up")   
print(todo_list)

#Assign_3
names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
names.reverse()              
print(names)

#Assign_4
numbers_random = [45, 12, 89, 33, 27]
numbers_random.sort(reverse=True)  
numbers_random.pop()               
print(numbers_random)

#Assign_5
cities = ["New York", "Paris", "Tokyo", "Sydney", "Cairo"]
cities.insert(2, "London")        
cities.append("Toronto")          
cities.reverse()                 
middle_index = len(cities) // 2
del cities[middle_index]         
print(cities)
