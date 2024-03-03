from Deck import Deck, Card
from Player import Player

class GameManager():
    def __init__(self):
        self.deck = Deck()

        self.player_1= Player("player 1")
        self.player_2= Player("player 2")
        self.pot = list()
        self.last_swiper = None


    def deal_four_cards(self,to:list):
        for i in range(4):
            to.append(self.deck.top_card())
    
    def check_swipe(self,card: Card, last_player):
        if not self.pot: # if pot is empty do nothing
            return False
        if card.v == self.pot[len(self.pot) - 1].v: # if last played card's value equal to top card in the pot enter the if
            last_player.pot_to_stash(self.pot)  
            self.last_swiper = last_player # initialize last_swiper
            last_player.stash.append(card) # add last played card to stash
            return True
        return False


    # append the card to pot
    def add_to_pot(self, card):
        self.pot.append(card)

        
        

