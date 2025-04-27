# Tip Calculator 
bill_amount = float(input("Enter the bill amount: "))
if bill_amount > 0:
    tip = bill_amount * 0.15
    total = bill_amount + tip

    print(f"Tip amount: ${tip:}")
    print(f"Total bill: ${total:}")


# Average Test Score Calculator 
score1 = float(input("Enter the first test score: "))
score2 = float(input("Enter the second test score: "))
score3 = float(input("Enter the third test score: "))
if score1 >= 0 and score2 >= 0 and score3 >= 0:
    average = (score1 + score2 + score3) / 3
    print(f"The average of your test scores is: {average:}")
    if average >= 90:
        print("Excellent work!")
    elif average >= 75:
        print("Good job!")
    else:
        print("Keep working hard!")

#Assign_3        
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 > num2:
    print(f"{num1} is larger than {num2}.")
elif num1 < num2:
    print(f"{num2} is larger than {num1}.")
else:
    print("Both numbers are equal.")
difference = num1 - num2
print(f"The difference between the numbers is {difference}.")