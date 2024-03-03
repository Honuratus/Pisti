from random import shuffle #Imports random

#Needed values for creating cards
values=[2,3,4,5,6,7,8,9,10,11,12,13,14]
suits = ["Hearts", "Spades", "Diamonds", "Clubs"]

class Card():
    #Initializes card class
    def __init__(self,value,suit):
        self.v = value
        self.s = suit
        
    #Represantation for standart output
    def __repr__(self): 
        return_str = None  
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
        #Creates all 52 cards
        super().__init__([Card(value, suit) for value in values for suit in suits])
        self.shuffle_deck()
    
    def shuffle_deck(self):
        shuffle(self)

    #Get the top card from deck and remove it
    def top_card(self):
        return self.pop() 



                