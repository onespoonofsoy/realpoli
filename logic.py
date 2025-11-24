import random
import tkinter as tk
import math
from bodies import Party

### IMPORTANT FUNCTIONS ###
# putty: receive numerical input within a range
def putty(ranger) -> int: 
    # print("VALID:", ranger)
    return_val = -1
    while True:
        try:
            return_val = int(input())
            if return_val not in ranger:
                print("Invalid input. try again: ",end="")
                continue
            break
        except ValueError:
            print("Invalid input, try again: ",end="")
    return return_val

### IMPORTANT VARIABLES ###
year = 1900
election_year = 1904
success_statements = [
    'sum ting wong',
    'It was hugely successful!',
    'It was successful!',
    'It wasn\'t that successful.',
]

### PLAYER SETUP ###
# Get player amount
print("Enter number of parties (2~8): ",end="")
player_amount = putty(range(2,9))
# 119 total seats if 7 players, 120 if not
total_seats = 120
if player_amount == 7: total_seats -= 1
# add players to roster
roster = []
for num in range(player_amount):
    name = input("Enter name of party " + str(num+1) + ": ")
    roster.append(Party(num+1, name, total_seats//player_amount))
# report successful setup
print("\nThere are", player_amount, "parties:")
for party in roster:
    print(party.name)
print()

### DISPLAY SETUP ###
display = tk.Tk()
display.title("Realpoli")

# --- STATS ---
top_frame = tk.Frame(display)
top_frame.pack(side="top", fill="x")

seats_text = f"Total Seats: {total_seats}"
seats_text += f"\nFor Majority: {math.ceil(total_seats / 2)}"
seats_text += f"\nFor 2/3: {math.ceil(total_seats*(2/3))}"

total_seats_label = tk.Label(top_frame, text = seats_text)
total_seats_label.pack(pady = 5)

# --- PARTY LIST ---
main_frame = tk.Frame(display)
main_frame.pack(fill="both", expand = True)

labels = []
for i, p in enumerate(roster):
    lbl = tk.Label(display, text="")
    lbl.pack()
    labels.append(lbl)

def update_display():

    for i, p in enumerate(roster):
        texterous = p.name + f" | ${p.money} |"
        texterous += f"Support: {p.support} | Seats: {p.seats}"
        labels[i].config(text = texterous)

    total_seats_label.config(text = seats_text)

    display.after(100, update_display)

update_display()

### MAIN LOOP ###
victory = False
election = False
snap_election = False
electoral_term = 4
while not victory:

    # announce year (PER-YEAR ACTIONS)
    if year == election_year:
        print("It's election year!")
        election_year += electoral_term
        election = True
    print('CURRENT YEAR:',year)
    print('NEXT ELECTION:', election_year,'\n')
    legislative_agenda = []

    # PER-PARTY ACTIONS
    for id in range(len(roster)):
        # recalculate variables and set party whose turn it is
        supports = [party.support for party in roster]
        support_sum = sum(supports)
        # avg = statistics.mean(supports)
        # std = statistics.stdev(supports)
        # print("Debugging: avg and std:", avg, std)
        party = roster[id]

        print(party.name)
        print("Money:", party.money, "// Support:", party.support,end= " //")
        # print(" Seats:",party.seats)
        print(f" Seats: {party.seats}/{total_seats}")
        print("Options:")
        print("1. Rally\n2. Fundraiser\n3. Propose legislation\n4. Skip")
        selection = putty(range(1,5))
        
        if selection == 1: # RALLY
            upper_limit = 1
            print("Choose rally size:")
            if party.money >= 100:
                print("1. Small: -$100, +~10 support")
                upper_limit += 1
            if party.money >= 500:
                print("2. Medium: -$500, +~50 support")
                upper_limit += 1
            if party.money >= 1000:
                upper_limit += 1
                print("3. Large: -$1000, +~100 support")
            if upper_limit == 1:
                print("Not enough money to hold a rally.")
                print("Your turn is skipped.\n")
                continue
            selection = putty(range(1,upper_limit)); print()
            size = '?'; money = 0; support = 0
            success_index = 2
            if selection == 1: # small rally
                size = 'SMALL'; money = 100
                modifier = random.randint(-2,10)
                support = 10 + modifier
                if modifier < 0: success_index = 3
                elif modifier >= 5: success_index = 1
            elif selection == 2: # medium rally
                size = 'MEDIUM'; money = 500
                modifier = random.randint(-10,50)
                support = 50 + modifier
                if modifier < 0: success_index = 3
                elif modifier >= 25: success_index = 1
            else: # large rally
                size = 'LARGE'; money = 1000
                modifier = random.randint(-20,100)
                support = 100 + modifier
                if modifier < 0: success_index = 3
                elif modifier >= 50: success_index = 1
            print(f"You held a {size} rally")
            print(success_statements[success_index])
            print(f"Money: -{money}, Support: +{support}")
            party.money -= money
            party.support += support

        elif selection == 2: # FUNDRAISER
            upper_limit = 0
            # print("Choose fundraiser size: 1. small, 2. medium, 3. large")
            # selection = putty(range(1,4)); print()
            selection = 1
            size = '?'; multiplier = 0; modifier = 0
            success_index = 2
            if selection == 1: # small fundraiser (ALL FUNDRAISERS)
                size = 'SMALL'; 
                multiplier = 1000
                modifier = random.randint(-500,500)
                if modifier <= -250: success_index = 3
                elif modifier >= 250: success_index = 1
            elif selection == 2: # medium fundraiser
                size = 'MEDIUM'
                multiplier = 5000
                modifier = random.randint(-2500, 2500)
                if modifier <= -1250: success_index = 3
                elif modifier >= 1250: success_index = 1
            else: # large rally
                size = 'LARGE'
                multiplier = 10000
                modifier = random.randint(-5000, 5000)
                if modifier <= -2500: success_index = 3
                elif modifier >= 2500: success_index = 1
            print(f"You held a fundraiser")
            print(success_statements[success_index])
            ### DEBUG
            '''
            print('Party Suppport:',party.support)
            print('Support Sum:', support_sum)
            print('Proportion', party.support/support_sum)
            print('Applied', multiplier * (party.support/support_sum))
            '''
            ### DEBUG
            money = int(multiplier * (party.support/support_sum) + modifier)
            print(f"Money: +{money}")
            party.money += money
        
        elif selection == 3: # PROPOSE LEGISLATION
            print("Choose legislation to propose: ")
            lawlist = [
                "1. Support a policy.", # not implemented yet
                "2. Denounce a policy.", # not implemented yet
                "3. Change election period.",
                "4. Call a snap election.",
                "5. Ban a party.", # not implemented yet
                "6. Grant emergency powers.", # not implemented yet
            ]
            for l in lawlist[2:]:
                print(l)
            bill = putty(range(2,7))
            legislative_agenda.append((bill,party))
        
        elif selection == 4: # SKIP (SURVEY)
            print('TURN SKIPPED')
            # print("survey not implemented yet")
        
        elif selection == 5: # PROPOSE LEGISLATION
            print('TURN SKIPPED')

        elif selection == 6: # SKIP
            print("TURN SKIPPED")
        
        else:
            print('ERROR')
            exit()
        
        print()

    # LEGISLATIVE SESSION

    # vote: vote on something
    def vote(roster, sponsor) -> bool:
        yea = 0; nay = 0; abstain = 0;
        yea_list = []
        nay_list = []
        abstain_list = []
        print('y: YEA / n: NAY / a: ABSTAIN')
        for party in roster:
            print(f"{party.name}, what is your vote? ::: ",end="")
            vota = ""
            while vota not in ['y','n','a']: vota = input()
            if vota == 'y': 
                yea += party.seats
                yea_list.append(party)
            elif vota == 'n': 
                nay += party.seats
                nay_list.append(party)
            else: 
                abstain += party.seats
                abstain_list.append(party)
        print('FINAL RESULTS')
        print('Yea:',yea,'Nay:',nay,'Abstain:',abstain)
        print("Yea:",yea_list)
        print("Nay:",nay_list)
        if abstain_list: print("Abstain:",abstain_list)
        if yea > nay: 
            print("The bill has passed.")
            sponsor.support += 200
            for yea_sayer in yea_list:
                yea_sayer.support += 50
            return True
        else: 
            print("The bill did not pass.")
            sponsor.support -= 50
            return False

    print(f"Legislative Session of {year}")
    for bill_proposal, sponsor in legislative_agenda:
        print()
        print("PROPOSAL: ",end="")
        if bill_proposal == 1:
            print("Motion to support")
            print("Not implemented yet")
        if bill_proposal == 2:
            print("Motion to denounce")
            print("Not implemented yet")
        if bill_proposal == 3:
            print("Motion to change electoral terms")
            print(f"{sponsor.name}, how many years should a term be?")
            proposed_term = putty(range(1,11))
            if vote(roster, sponsor):
                print("The electoral term is now",proposed_term,"years.")
                print("This shall take effect after the next election.")
                electoral_term = proposed_term
        if bill_proposal == 4:
            print("Motion to call a snap election")
            if vote(roster, sponsor):
                print("Snap elections shall take place.")
                election = True
                snap_election = True
        if bill_proposal == 5:
            print("Motion to ban a party")
            print("Not implemented yet")
        if bill_proposal == 6:
            print("Motion to grant emergency powers to")
            print("Not implemented yet")
    print()

    # ELECTIONS
    if election:

        if snap_election: 
            print("SNAP ",end="")
            election_year = year + electoral_term

        print("ELECTION OF", year)
        support_sum = sum([p.support for p in roster])
        for party in roster:
            party.seats = round((party.support / support_sum) * total_seats)
        roster.sort(key = lambda p: p.seats, reverse = True)
        for party in roster:
            print(f"{party.name}: {party.seats} Seats")
        
        print('DEBUG:', sum([p.seats for p in roster]))

        election = False
    
    print()
    year += 1
    
### ENDGAME ###
if victory: 
    print("GAME OVER: Placeholder WINS")

# write results here