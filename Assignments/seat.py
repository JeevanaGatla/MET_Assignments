#Plane Seat Reservation System
 
seats = [
    ["1A", "1B", "1C"],
    ["2A", "2B", "2C"],
    ["3A", "3B", "3C"]
]
 
def print_seats():
    for row in seats:
        print(" ".join(row))
total = 9
booking = 0
 
while booking < total:
    choosen_seat = input("Enter the seat number:")
    
    for i in range(3):
        for j in range(3):
            if seats[i][j] == choosen_seat:
                seats[i][j] = 'X'
                booking += 1
    print_seats()