name=input("Enter your name:")
print(name)
dish=input("Your favourite dish:")
print(dish)
print("Hi"+ name+ "Your favourite dish is"+ dish)


colors = ("yellow", "white", "black")
colors_list = list(colors)
print(colors_list)


name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
print(f"Hello {name}, you will be {age + 5} years old after 5 years.")


name = input("Please enter your name: ")
math_score = int(input("Please enter your math score: "))
english_score = int(input("Please enter your English score: "))
print("{} scored {} in math and {} in English.".format(name, math_score, english_score))


name = input("Please enter your name: ")
print(f"""
     Dear {name},
     Thank you for reaching out to us. We appreciate your time and interest.
     Best regards,
     [Your Name]
     """)