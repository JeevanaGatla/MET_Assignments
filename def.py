# Assign 1
def add(a, b):
    print(f"Result: {a} + {b} = {a + b}")
def subtract(a, b):
    print(f"Result: {a} - {b} = {a - b}")
def multiply(a, b):
    print(f"Result: {a} * {b} = {a * b}")
def divide(a, b):
    if b != 0:
        print(f"Result: {a} / {b} = {a / b}")
    else:
        print("Error: Cannot divide by zero.")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

if operation == '+':
    add(num1, num2)
elif operation == '-':
    subtract(num1, num2)
elif operation == '*':
    multiply(num1, num2)
elif operation == '/':
    divide(num1, num2)
else:
    print("Invalid operation.")

# Assign 2
def check_even_odd(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

number = int(input("Enter a number to check even or odd: "))
check_even_odd(number)

# Assign 3
def display_student_info(name, grade):
    print(f"Name: {name}")
    print(f"Grade: {grade}")

student_name = input("Enter student name: ")
student_grade = input("Enter student grade: ")
display_student_info(student_name, student_grade)

# Assign 4
def generate_table(number):
    print(f"Multiplication table for {number}:")
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

table_number = int(input("Enter a number to generate multiplication table: "))
generate_table(table_number)
