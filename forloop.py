#Assign_1
numbers_list=[10,22,33,67,89,83]
number=int(input("Enter a number: "))
for i in numbers_list:
   if i==number:
      print("Found the number")
   break
else:
    print("Not found your number")


# Assign 2
password = 'secret123'
attempts = 3

while attempts > 0:
    user = input("Guess the password: ")
    if user == password:
        print("Access Granted")
        break
    else:
        attempts -= 1
        print(f"Wrong password! Attempts left: {attempts}")
else:
    print("Access Denied")