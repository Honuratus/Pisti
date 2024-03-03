class Player():
    def __init__(self, username):
        self.stash = list()
        self.hand = list()
        self.username = username 
        self.total_points = 0
        self.jocker_pisti = 0
        self.normal_pisti = 0

    #It gets the top card from players hand and removes it from hand and then returns it
    def play_card(self, idx): 
        temp = self.hand[idx]
        self.hand.remove(temp)
        return temp
    
    #Copys the pot to stash and clear entire pot
    def pot_to_stash(self, pot): 
        self.stash.extend(pot)
        pot.clear()


