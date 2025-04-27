#1
def calculate_bill(a, b):
    c = a * b
    return c 
hours = int(input("Enter hours: "))
pay = int(input("Enter pay per hour: "))
bill = calculate_bill(hours, pay)
print(f"Your bill is: {bill}")
 

#2
def calculate_bill(hours, pay):
    total_bill = hours * pay
    return total_bill
def calculate_tax(total_bill):
    tax = 15
    total_bill_after_tax = total_bill + tax
    return total_bill_after_tax
total_bill = calculate_bill(5, 700)
total_bill_after_tax = calculate_tax(total_bill)
print(total_bill_after_tax)
 