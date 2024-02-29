from Deck import Deck


class Player():
    def __init__(self, username):
        self.stash = list()
        self.hand = list()
        self.username = username
        self.total_points = 0

    def play_card(self, idx):
        temp = self.hand[idx]
        self.hand.remove(temp)
        return temp

    def pot_to_stash(self, pot):
        # pot bir list append olunacak
        for card in pot:
            self.stash.append(card)
            pot.pop()


