from random import shuffle

values=["2","3","4","5","6","7","8","9","10","11","12","13","14"]
suits = ["Hearts", "Spades", "Diamonds", "Clubs"]

class Card():
    def __init__(self,value,suit):
        self.v = value
        self.s = suit

    def __repr__(self):
        return f"{self.v} of {self.s}"
    

class Deck(list):
    def __init__(self):
        super().__init__()
        self.total_card_amount = 52
        
    def create_deck(self):
      for suit in suits:
            for value in values:
                new_card = Card(value, suit)
                self.append(new_card)
    
    def shuffle_deck(self):
        shuffle(self)
    
    def top_card(self):
        return self.pop()



                