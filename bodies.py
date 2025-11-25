class Party:
    def __init__(self, id, name, seats):
        self.id = id
        self.name = name
        self.seats = seats
        self.support = 100
        self.money = 2000
        self.debt = 0
        self.debt_interest = 0.0
        self.instability = 0