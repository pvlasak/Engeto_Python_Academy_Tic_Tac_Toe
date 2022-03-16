# This is a main script of "Tic Tac Toe" Game

from tic_tac_toe_functions import *
import random


def ttt_main():
    print("Welcome to Tic Tac Toe")
    print(delimiter)
    print(rules)
    print(delimiter)
    print("Let's start the game")
    print(delimiter)
    play_board = create_sq_board()
    player_id = random.choice((0, 1))
    plot_sq_board(play_board)
    while lst_of_pos:
        update_sq_board(player_id, play_board)
        plot_sq_board(play_board)
        game_winner = check_winner(player_id, play_board)
        if game_winner:
            print(f"{player_names[player_id]} won!")
            quit()
        else:
            player_id = switch_player(player_id)
            continue
    else:
        print("Game Over.")
        quit()
# Press the green button in the gutter to run the script.


if __name__ == '__main__':
    ttt_main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
