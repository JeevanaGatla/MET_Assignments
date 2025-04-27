#Assign_1

my_games = {"cricket", "football", "tennis"}
friend_games = {"badminton", "cricket", "chess"}
all_games = my_games.union(friend_games)
print("All unique games:", all_games)

#Assign_2

games = {"badminton", "cricket", "chess"}
games.discard("throwball") 
print("After discard:", games)


#Assign_3

my_games = {"cricket", "football", "tennis"}
friend_games = {"badminton", "cricket", "chess"}
only_my_games = my_games.difference(friend_games)
print("Games only I play:", only_my_games)

#Assign_4

my_games = {"cricket", "football", "tennis"}
my_games.clear()  
my_games.update(["baseball", "golf", "tennis"])  # add new items
copied_games = my_games.copy()
print("Updated & copied set:", copied_games)
