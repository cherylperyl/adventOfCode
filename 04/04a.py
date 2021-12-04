def check_win(board):
    for i in range(5):
        if board[i][0] == "x":
            row = [board[i][j] for j in range(1,5)]
            for i in range(4):
                if row[i] != "x":
                    break
                if i == 3:
                    return True
    for i in range(5):
        if board[0][i] == "x":
            column = [board[j][i] for j in range(1,5)]
            for i in range(4):
                if column[i] != "x":
                    break
                if i == 3:
                    return True
    return False

order = []
one_board = []
all_boards = []
with open("input.txt") as f:
    for line in f:
        line = line.strip("\n")
        if order == []:
            order = line.split(",")
        else:
            if line == "":
                all_boards.append(one_board)
                one_board = []
            else:
                one_board.append(line.split())
all_boards = all_boards[1:]

def any_win(all_boards):
    for i in range(len(all_boards)):
        if check_win(all_boards[i]):
            return i
    return False

last_number_called = None
while not any_win(all_boards):
    current_number = order[0]

    for board in all_boards:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == current_number:
                    board[i][j] = "x"
    
    last_number_called = int(order[0])
    order = order[1:]

winning_board_num = any_win(all_boards)
marked_board = all_boards[winning_board_num]

sum = 0
for i in range(5):
    for j in range(5):
        if marked_board[i][j] != "x":
            sum += int(marked_board[i][j])
print(sum*last_number_called)




            

