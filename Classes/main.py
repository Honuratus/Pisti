from GameManager import GameManager


def main():
    game_manager = GameManager() # create instance of GameManager class
    game_manager.deal_four_cards(game_manager.pot) # deal four cards to pot

    while len(game_manager.deck)!=0: # main game loop (exits if deck is empty)
        game_manager.deal_four_cards(game_manager.player_1.hand) # give player 4 card
        game_manager.deal_four_cards(game_manager.player_2.hand) # give 4 card to other player
        while len(game_manager.player_2.hand)!=0: # manage the current hand (if player 2 plays the it's last card exit the loop)
            
            # print pot and hand
            print("Pot: ")
            print(game_manager.pot)
            print()
            print(game_manager.player_1.hand)

            # get index of played card
            idx = int(input("(Player1)Select from upper list:"))

            # pop up from player hand
            played_card = game_manager.player_1.play_card(idx)
            
            # check for swipe if check_swipe returns false then add card to pot
            if game_manager.check_swipe(played_card, game_manager.player_1):
                pass
            else:
                game_manager.add_to_pot(played_card) 

            # print pot and hand
            print()
            print("Pot: ")
            print(game_manager.pot)
            print()
            print(game_manager.player_2.hand)

            # get index of played card
            idx = int(input("(Player2)Select from upper list:"))

            played_card = game_manager.player_2.play_card(idx)

            # check for swipe if check_swipe returns false then add card to pot
            if game_manager.check_swipe(played_card, game_manager.player_2):
                pass
            else:
                game_manager.add_to_pot(played_card)


    if len(game_manager.pot)!=0:
        print("pipiiii\n\n")
        game_manager.last_swiper.pot_to_stash(game_manager.pot)

    if len(game_manager.player_1.stash)>len(game_manager.player_2.stash):
        print("Player One Won")

    elif len(game_manager.player_1.stash)<len(game_manager.player_2.stash):
        print("Player Two Won")

    else:
        print("Tie")
    
if __name__ == "__main__":
    main()


