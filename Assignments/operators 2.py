#Assign_1

num = int(input("Enter a number: "))
if num % 2 == 0:
   print("Even")
else:
   print("Odd")

#Assign_3

num = int(input("Enter a number: "))
if num > 0:
   print("Positive")
elif num < 0:
   print("Negative")
else:
   print("Zero")

#Assign_3

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
largest = max(num1, num2, num3)
print("The largest number is:", largest)

#Assign_4

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
if num1 >= num2 and num1 >= num3:
   print("The largest number is:", num1)
elif num2 >= num1 and num2 >= num3:
   print("The largest number is:", num2)
else:
   print("The largest number is:",num3)
