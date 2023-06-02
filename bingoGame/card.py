import random as r


class PlayerCard:

    def __init__(self):
        self.list_b = []
        self.list_i = []
        self.list_n = []
        self.list_g = []
        self.list_o = []
        self.card_list = [self.list_b, self.list_i, self.list_n, self.list_g, self.list_o]

    def generate_card(self):
        for x in range(0, 5):
            self.list_b.append(r.randrange(1, 15 + 1))

        for x in range(0, 5):
            self.list_i.append(r.randrange(16, 30 + 1))

        for x in range(0, 5):
            self.list_n.append(r.randrange(31, 45 + 1))

        for x in range(0, 5):
            self.list_g.append(r.randrange(46, 60 + 1))

        for x in range(0, 5):
            self.list_o.append(r.randrange(61, 75 + 1))

    def print_card(self):
        print("B I N G O")
        for x in:
