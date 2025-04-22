#Assign_1
colors_list = ["red", "yellow", "green", "blue", "black"]
colors_tuple = tuple(colors_list)              
print(colors_list)
print("Tuple:", colors_tuple)
colors_list = list(colors_tuple)               
colors_list.append("white")                    
colors_tuple = tuple(colors_list)              
print("Updated Tuple:", colors_tuple)

#Assign_2
t1 = (10, 20, 20)
t2 = (40, 50, 60)
t3 = t1 + t2                                
print("t3:", t3)

#Assign_3
letters = ("A", "B", "C")
repeated_letters = letters * 3                
print("Repeated Tuple:", repeated_letters)

#Assign_4
animals = ("dog", "cat", "elephant", "lion", "tiger")
animals_list = list(animals)                   
animals_list.remove("elephant")               
animals_list.append("cheetah")                
animals = tuple(animals_list)                
print("Final Animals Tuple:", animals)
