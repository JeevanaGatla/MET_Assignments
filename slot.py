#parking slot

parking_slot = [
    ["1A","1B"] ,
    ["2A","2B"],  
    ["3A","3B"]
]
def print_slots():
    for row in parking_slot:
        print(" ".join(row))

total = 6
booking = 0
 
while booking < total:
    choosen_slot = input("Enter the parking slot:")
    
    for i in range(3):
        for j in range(2):
            if parking_slot[i][j] == choosen_slot:
               parking_slot[i][j] ='X'
               booking += 1
                 
            print_slots()
   