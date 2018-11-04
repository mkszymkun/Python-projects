board = [['   ','   ','   '],
		['   ','   ','   '],
		['   ','   ','   ']]

def PrintBoard(board):
	for i in range(0,3):
		print(board[i][0] + '|' + board[i][1] + '|' + board[i][2])
		if i != 2:
			print('-----------')

def UpdateBoard(x, y, board, player):
	board[x][y] = player

def CheckWinCondition(board, player):
	for i in range(0,3):
		if board[i][0] == player and  board[i][1] == player and board[i][2] == player:
			return player
		elif board[0][i] == player and  board[1][i] == player and board[2][i] == player:
			return player
	if board[0][0] == player and  board[1][1] == player and board[2][2] == player:
		return player
	elif board[0][2] == player and  board[1][1] == player and board[2][0] == player:
		return player
	else:
		return 'nope'

player1 = ' X '
player2 = ' O '
player = player2

for i in range(0,50):
	print()

print("TIC TAC TOE")
PrintBoard(board)

while CheckWinCondition(board, player) == 'nope':

	if player == player1:
		player = player2
	else:
		player = player1

	valid_input = False

	while valid_input == False:
		print('Player {} is playing'.format(player))
		x = int(input('Enter a row (1 - 3)'))
		y = int(input('Enter a column (1 - 3)'))
		if x > 0 and x < 4 and y > 0 and y < 4:
			if board[x - 1][y - 1] == '   ':
				valid_input = True

	UpdateBoard(x - 1, y - 1, board, player)
	for i in range(0,50):
		print()
	PrintBoard(board)

print('Player {} won!'.format(player))