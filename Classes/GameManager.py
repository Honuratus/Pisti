from Deck import Deck
from Player import Player

class GameManager():
    def __init__(self):
        self.deck = Deck()
        self.deck.create_deck()
        self.deck.shuffle_deck()

        self.player_1= Player("player 1")
        self.player_2= Player("player 2")
        self.pot = list()
        self.last_swiper = None


    def deal_four_cards(self,to:list):
        for i in range(4):
            to.append(self.deck.top_card())
    

    def check_swipe(self,card, last_player):
        print(self.pot[len(self.pot) - 1].v)
        if int(card.v) == int(self.pot[0].v):
            last_player.pot_to_stash(self.pot)
            self.last_swiper = last_player
        if card.v=="Jack":
            last_player.pot_to_stash(self.pot)
            self.last_swiper = last_player


    def add_to_pot(self, card):
        self.pot.append(card)

        
        

        # deck ten 4 defa top_card fonksiyonunu çağırman ve her seferinde onu hangi parametre geldiyse ona append etmen
