dimension = int(3)
num_players = int(2)

rules = """
        GAME RULES:
        Each player can place one mark (or stone)
        per turn on the 3x3 grid. The WINNER is
        who succeeds in placing three of their
        marks in a:
        * horizontal,
        * vertical or
        * diagonal row."""

delimiter = "=" * 50
board_dm = "+-+-+-+"

lst_of_pos = [pos + 1 for pos in range(dimension ** 2)]
player_names = ('Player X', 'Player O')
player_ids = [pid for pid in range(num_players)]
player_symbols = ['x', 'o']


def create_sq_board():
    board = []
    for i in range(dimension):
        line = []
        for cell in range(dimension):
            line.append("-")
        board.append(line)
    return board


def plot_sq_board(board):
    board_plt = []
    for line in range(dimension):
        board_plt.append("|".join(board[line]))
    for row in range(dimension):
        print(board_dm)
        print(f"|{board_plt[row]}|")


def update_sq_board(current_player_id, board):
    print(delimiter)
    verification = True
    while verification:
        number = input(f"|{player_names[current_player_id]} | Please enter your move number: ")
        if number.isnumeric() and int(number) < 10:
            if int(number) in lst_of_pos:
                print(delimiter)
                symbol = player_symbols[current_player_id]
                i_row = int((int(number) - 1) / dimension)
                j_column = int((int(number) - 1) % dimension)
                board[i_row][j_column] = symbol
                lst_of_pos.pop(lst_of_pos.index(int(number)))
                verification = False
            else:
                print("Position number is already occupied. Select a new number.")
        else:
            print("Input is not numeric or has more than 2 digits.")
    return board


def switch_player(current_player_id):
    if current_player_id % num_players == 0:
        next_plr_id = 1
    else:
        next_plr_id = 0
    return next_plr_id


def check_winner(current_player_id, board):
    winner = [check_rows(current_player_id, board), check_cols(current_player_id, board),
              check_pr_dg(current_player_id, board), check_sec_dg(current_player_id, board)]
    if True in winner:
        status = True
    else:
        status = False
    return status


def check_rows(current_player_id, board):
    result = False
    for i in range(dimension):
        check_list = board[i]
        count = check_list.count(player_symbols[current_player_id])
        if count == 3:
            result = True
            break
    return result


def check_cols(current_player_id, board):
    result = False
    for j in range(dimension):
        check_list = []
        for i in range(dimension):
            check_list.append(board[i][j])
            count = check_list.count(player_symbols[current_player_id])
            if count == 3:
                result = True
                break
    return result


def check_pr_dg(current_player_id, board):
    check_list = []
    result = False
    for i in range(dimension):
        check_list.append(board[i][i])
        count = check_list.count(player_symbols[current_player_id])
        if count == 3:
            result = True
        break
    return result


def check_sec_dg(current_player_id, board):
    check_list = []
    result = False
    for i in range(dimension):
        j = int((dimension - 1) - i)
        check_list.append(board[i][j])
        count = check_list.count(player_symbols[current_player_id])
        if count == 3:
            result = True
            break
    return result
