class Party:

    def __init__(self, id, name, seats):
        self.id = id
        self.name = name
        self.seats = seats

player_amount = int(input("Enter number of parties (1~8): "))
print(player_amount)
while player_amount not in (1,2,3,4,5,6,7,8,9):
    print("Not an acceptable number of parties.")
    player_amount = int(input("Enter number of parties (1~8): "))

total_seats = 120
if player_amount == 7: total_seats = 119

roster = []

for num in range(player_amount):
    name = input("Enter name of party " + str(num+1) + ": ")
    roster.append(Party(num+1,name,total_seats//player_amount))

print("There are", player_amount, "parties.")
print("The parties are:")
for party in roster:
    print(party.name)
    
    