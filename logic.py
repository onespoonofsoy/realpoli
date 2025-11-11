class Party:
    def __init__(self, id, name, seats, support):
        self.id = id
        self.name = name
        self.seats = seats
        self.support = support
        self.money = 2000

year = 1900

### START GAME SETUP SECTION

# Get player amount
player_amount = int(input("Enter number of parties (2~8): "))
print(player_amount)
while player_amount not in range(2,9):
    print("Not an acceptable number of parties.")
    player_amount = int(input("Enter number of parties (2~8): "))

# Determine initial total number of seats
total_seats = 120
if player_amount == 7: total_seats = 119

# add players to roster
roster = []
for num in range(player_amount):
    name = input("Enter name of party " + str(num+1) + ": ")
    roster.append(Party(num+1, name, total_seats//player_amount, 0))

# report successful setup
print("\nThere are", player_amount, "parties.")
print("The parties are:")
for party in roster:
    print(party.name)
print()

### END GAME SETUP SECTION

# START MAIN GAME LOOP
victory = False
while not victory:
    for id in range(len(roster)):
        party = roster[id]
        print("Turn:",party.name)
        print("Money:", party.money, "// Support:", party.support)
        print("Options:")
        print("1.Rally\n2.Fundraiser\n3.Sabotage\n4.Survey\n5. Skip")
        selection = 0
        while selection not in range(1,6): selection = int(input())
        if selection == 1: # rally
            print("rally")
        if selection == 2: # fundraiser
            print("fundraiser")
        if selection == 3: # sabotage
            print("sabotage")
        if selection == 4: # survey
            print("survey")
        if selection == 5: # skip
            print('alrighty then')
        print()
    
# END MAIN GAME LOOP

if victory: print("Placeholder wins!")

# write results here