#Assign_1
print("Numbers from 30 to 40:")
num = 30
while num <= 40:
    print(num)
    num += 1
print("\n")  

#Assign_2
guess = int(input("Guess the number: "))
if guess == 7:
    print("Correct!")
else:
    print("Incorrect")
print("\n")


#Assign_3
print("Even numbers from 2 to 20:")
even_num = 2
while even_num <= 20:
    print(even_num)
    even_num += 2
print("\n")


#Assign_4
print("Enter numbers to sum (enter 0 to stop):")
total = 0
while True:
    number = int(input())
    if number == 0:
        break
    total += number
print(f"The sum of all numbers entered is: {total}")
