#Assign_4

temperature = float(input("Enter the current temperature in Celsius: "))
is_raining = input("Is it raining? (yes/no): ")
if temperature > 30:
    if is_raining == "yes":
        print("Stay indoors and watch a movie.")
    else:
        print("Go swimming.")
elif 20 < temperature <= 30:
    if is_raining == "yes":
        print("Visit a museum.")
    else:
        print("Perfect for a picnic!")
elif 10 < temperature <= 20:
    if is_raining == "yes":
        print("Indoor sports recommended.")
    else:
        print("Go for a walk.")
else: 
    if is_raining == "yes":
        print("Stay home with hot chocolate.")
    else:
        print("Ice skating would be fun!")



 #Assign_5

membership = input("Are you a member? (yes/no): ")
purchase_amount = int(input("Enter the total purchase amount: "))
coupon_code = input("Enter the coupon code : ")
discount = 0
if membership == "yes":
    if purchase_amount > 100:
        discount = 20
    else:
        discount = 10
    if coupon_code == "special":
        discount += 5
else:  
    if purchase_amount > 200:
        discount = 10
    else:
        if coupon_code == "special":
            discount = 5

final_price = purchase_amount * (1 - discount / 100)
print(f"Final price after discount: ${final_price:}")