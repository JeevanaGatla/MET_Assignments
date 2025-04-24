#Assign_1

science = input("Do you have 90+ in science? (True/False): ")
social = input("Do you have 90+ in social? (True/False): ")
maths = input("Do you have 90+ in maths? (True/False): ")
has_A_in_all = (science == "True" and social == "True" and maths == "True")
print("Has A grade in all subjects:", has_A_in_all)


#Assign_2

sentence = input("Enter a sentence: ")
word = input("Enter a word to search in the sentence: ")
word_in_sentence = word in sentence
print(word_in_sentence)


#Assign_3

taken_usernames = ["alice", "bob", "charlie"]
new_username = input("Enter a new username: ")
is_taken = new_username in taken_usernames
print(is_taken)


#Assign_4

password = input("Enter a password: ")
valid_password = any(char in "@#$%&" for char in password) and not password.isspace()
print("Valid password:", valid_password)
