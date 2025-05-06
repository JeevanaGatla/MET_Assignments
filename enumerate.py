#1
shopping_list = ["almond milk", "bread", "milk chocolate", "eggs", "milk"]
for i,k in enumerate(shopping_list):
    print(f"{i+1} . {k} ")
def count_milk_items(shopping_list):
    count = 0
    for item in shopping_list:
        if "milk" in item.lower():  
            count += 1
    return count
milk_count=count_milk_items(shopping_list)
print(f"Milk related products:{milk_count}")  


#2
inventory = {
 "apple": 10,
 "banana": 25,
 "orange": 15,
 "grape": 8
}
user_product = input("Enter the product name = ")
for key in inventory:
    if user_product == key:
        print(f"{inventory[key]}  {user_product}'s are avilable ")
        break
else:  
    print("Inventory not found")


#3
sentence = "Learning Python is fun"
words = sentence.split()
for word in words:
  reversed_word = word[::-1]
  print(reversed_word)
  



#4
temps = (30, 32, 31, 29, 28, 33, 34)
days =("Monday","Tuesday","wednesday","thursday","friday","saturday","sunday")
for i,k in enumerate(temps):
    print ( f" Day {i+1} ({days[i]}) : {k}°C ")
    



#5
import time
for i in range(10, -1, -1):
    print(i)
    time.sleep(1)
print("Time's up") 