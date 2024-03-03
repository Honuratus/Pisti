class Player():
    def __init__(self, username):
        self.stash = list()
        self.hand = list()
        self.username = username 
        self.total_points = 0 # for future updates
        self.jocker_pisti = 0
        self.normal_pisti = 0

    # it's get the top card from player hand and remove it from hand and then return it
    def play_card(self, idx): 
        temp = self.hand[idx]
        self.hand.remove(temp)
        return temp

    def pot_to_stash(self, pot): # copy the pot to stash and clear entire pot
        self.stash.extend(pot)
        pot.clear()


