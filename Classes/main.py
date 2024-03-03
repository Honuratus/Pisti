from GameManager import GameManager


def main():
    game_manager = GameManager() #Creates instance of GameManager class
    game_manager.deal_four_cards(game_manager.pot) #Deal four cards to pot

    while len(game_manager.deck)!=0: #Main game loop (exits if deck is empty)
        game_manager.deal_four_cards(game_manager.player_1.hand) #Gives player 4 card
        game_manager.deal_four_cards(game_manager.player_2.hand) #Gives 4 card to other player
        while len(game_manager.player_2.hand)!=0: #Manage the current hand (if player 2 plays the it's last card exit the loop)
            
            #Prints pot and hand
            print("Pot: ")
            print(game_manager.pot)
            print()
            print(game_manager.player_1.hand)

            #Gets index of played card
            idx = int(input("(Player1)Select from upper list:"))

            #Pop up from player hand
            played_card = game_manager.player_1.play_card(idx)
            
            #Checks for swipe if check_swipe returns false then add card to pot
            if game_manager.check_swipe(played_card, game_manager.player_1):
                pass
            else:
                game_manager.add_to_pot(played_card) 

            #Prints pot and hand
            print()
            print("Pot: ")
            print(game_manager.pot)
            print()
            print(game_manager.player_2.hand)

            #Gets index of played card
            idx = int(input("(Player2)Select from upper list:"))

            played_card = game_manager.player_2.play_card(idx)

            #Chhecks for swipe if check_swipe returns false then add card to pot
            if game_manager.check_swipe(played_card, game_manager.player_2):
                pass
            else:
                game_manager.add_to_pot(played_card)


    game_manager.calc_points(game_manager.player_1, game_manager.player_2)
    game_manager.calc_points(game_manager.player_2, game_manager.player_1)


    print(f"\n\tP1:{game_manager.player_1.total_points}\t\n")
    print(f"p1 pisti {game_manager.player_1.jocker_pisti}\n p1 j pist: {game_manager.player_1.normal_pisti}")
    print(f"P1 Stash{game_manager.player_1.stash}")
    print(f"\n\tP2:{game_manager.player_2.total_points}\t\n")
    print(f"p2 pisti {game_manager.player_2.jocker_pisti}\n p2 j pist: {game_manager.player_2.normal_pisti}")
    print(f"P2 Stash{game_manager.player_2.stash}")


    if game_manager.player_1.total_points>game_manager.player_2.total_points:
        print("Player One Won")

    elif game_manager.player_1.total_points<game_manager.player_2.total_points:
        print("Player Two Won")

    else:
        print("Tie")
    
if __name__ == "__main__":
    main()


