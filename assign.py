sentence = input("Enter a sentence: ")
p_count = sentence.count('p')
is_alnum = sentence.isalnum()
print(f"The letter 'p' appears {p_count} times.")
print(f"The sentence contains only alphabets and numbers: {is_alnum}")




user_input = input("Enter any string: ")
print(f"isupper(): {user_input.isupper()}")
print(f"islower(): {user_input.islower()}")
print(f"isdigit(): {user_input.isdigit()}")
print(f"isalnum(): {user_input.isalnum()}")



text = "Python is easy. Python is powerful"
modified_text = text.replace("Python", "Coding").upper()
print("Modified text:", modified_text)



sentence2 = input("Enter a sentence: ")
clean_sentence = sentence2.strip()
the_count = clean_sentence.lower().count("the")
print("Cleaned sentence:", clean_sentence)
print(f"Count of 'the': {the_count}")



first_name = input("Enter your first name: ")
middle_name = input("Enter your middle name: ")
last_name = input("Enter your last name: ")
formatted_name = f"Mr. {first_name} {middle_name} {last_name}"
print("Formatted Name:", formatted_name)
