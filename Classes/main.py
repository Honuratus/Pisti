from GameManager import GameManager


def main():
    game_manager = GameManager()
    game_manager.deal_four_cards(game_manager.pot) # deal four cards to pot

    while len(game_manager.deck)!=0:
        game_manager.deal_four_cards(game_manager.player_1.hand)
        game_manager.deal_four_cards(game_manager.player_2.hand)
        while len(game_manager.player_2.hand)!=0:
            print("Pot: ")
            print(game_manager.pot[len(game_manager.pot) - 1])
            print()
            print(game_manager.player_1.hand)

            idx = int(input("(Player1)Select from upper list:"))


            played_card = game_manager.player_1.play_card(idx)
            game_manager.add_to_pot(played_card)
            game_manager.check_swipe(played_card, game_manager.player_1)
            print()
            print("Pot: ")
            print(game_manager.pot[len(game_manager.pot) - 1])
            print()
            print(game_manager.player_2.hand)
            idx = int(input("(Player2)Select from upper list:"))

            played_card = game_manager.player_2.play_card(idx)
            game_manager.add_to_pot(played_card)
            game_manager.check_swipe(played_card, game_manager.player_2)

    if len(game_manager.pot)!=0:
        game_manager.last_swiper.pot_to_stash(game_manager.pot)

    if len(game_manager.player_1.stash)>len(game_manager.player_2.stash):
        print("Player One Won")

    elif len(game_manager.player_1.stash)<len(game_manager.player_2.stash):
        print("Player Two Won")

    else:
        print("Tie")
    
if __name__ == "__main__":
    main()


