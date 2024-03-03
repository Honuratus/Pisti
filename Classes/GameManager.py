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
        if not self.pot: #If pot is empty does nothing
            return False
        if card.v == self.pot[len(self.pot) - 1].v or card.v == 11: #If last played card's value equals to top card in the pot enters the if
            last_player.pot_to_stash(self.pot)  
            self.last_swiper = last_player #Initializes last_swiper
            last_player.stash.append(card) #Adds last played card to stash
            if len(self.pot) == 1:
                if card.v == 11:
                    last_player.total_points+=50
                    last_player.jocker_pisti += 1
                else:
                    last_player.total_points+=10
                    last_player.normal_pisti += 1
            return True
        return False


    #Append the card to pot
    def add_to_pot(self, card):
        self.pot.append(card)

    #Point calculation system
    def calc_points(self, player, other_player):
        for card in player.stash:
            print(player.total_points)
            if card.v==11:
                player.total_points+=1
            if card.v==14:
                player.total_points+=1
            if card.v==2 and card.s=="Clubs":
                player.total_points+=2
            if card.v==10 and card.s=="Diamonds":
                player.total_points+=3
        if len(player.stash)>len(other_player.stash):
            player.total_points+=3
            




        
        

