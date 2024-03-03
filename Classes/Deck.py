from random import shuffle

values=[2,3,4,5,6,7,8,9,10,11,12,13,14]
suits = ["Hearts", "Spades", "Diamonds", "Clubs"]

class Card():
    def __init__(self,value,suit):
        self.v = value
        self.s = suit

    def __repr__(self): # represantation for standart output
        return_str = None # str 
        if self.v == 11:
            return_str = f"Jack of {self.s}"
        elif self.v == 12:
            return_str = f"Queen of {self.s}"
        elif self.v == 13:
            return_str = f"King of {self.s}"
        elif self.v == 14:
            return_str =  f"Ace of {self.s}"
        else:
            return_str = f"{self.v} of {self.s}"

        return return_str
    

class Deck(list):
    def __init__(self):
        super().__init__()
        
    def create_deck(self): # for loop wil be edited
      for suit in suits:
            for value in values:
                new_card = Card(value, suit)
                self.append(new_card)
    
    def shuffle_deck(self): # from random shuffle
        shuffle(self)
    
    def top_card(self):
        return self.pop() # get the top card from deck and remove it



                