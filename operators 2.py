num = int(input("Enter a number: "))
if num % 2 == 0:
   print("Even")
else:
   print("Odd")


num = int(input("Enter a number: "))
if num > 0:
   print("Positive")
elif num < 0:
   print("Negative")
else:
   print("Zero")


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
largest = max(num1, num2, num3)
print("The largest number is:", largest)



num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
if num1 >= num2 and num1 >= num3:
   print("The largest number is:", num1)
elif num2 >= num1 and num2 >= num3:
   print("The largest number is:", num2)
else:
   print("The largest number is:",num3)