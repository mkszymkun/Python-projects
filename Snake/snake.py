import random

size = 5

board = [[' ']*size for i in range(size)]

current_head_rows = []
current_head_cols  = []
current_head = 1

current_tail = 0

candy_rows = []
candy_cols = []
candy = False
current_candy = 0

playing = True
score = 0

def PrintBoard():
	global size
	global score
	print("SCORE: {}\n".format(score))
	print('---'*size)
	for i in range(0,size):
		print('|', end = ' ')
		for j in range(0,size - 1):
			print(board[i][j] + '|', end=' ')
		print(board[i][size - 1] + '|')
		print('---'*size)

def StartingPosition():
	global size
	head_position_row = random.randint(0, size - 1)
	head_position_col = random.randint(0, size - 1)
	board[head_position_row][head_position_col] = '@'

	valid_tail_position1 = [head_position_row,head_position_col - 1]
	valid_tail_position2 = [head_position_row,head_position_col + 1]
	valid_tail_position3 = [head_position_row - 1,head_position_col]
	valid_tail_position4 = [head_position_row + 1,head_position_col]
	valid_tail_positions = [valid_tail_position1, valid_tail_position2, valid_tail_position3, valid_tail_position4]
	valid_tail = False

	while not valid_tail:
		tail_position = random.choice(valid_tail_positions)
		tail_position_row = tail_position[0]
		tail_position_col = tail_position[1]
		if (tail_position_row >= 0 and tail_position_row < size and
			tail_position_col >= 0 and tail_position_col < size):
			valid_tail = True
			board[tail_position_row][tail_position_col] = '#'
			current_head_rows.append(tail_position_row)
			current_head_cols.append(tail_position_col)

	current_head_rows.append(head_position_row)
	current_head_cols.append(head_position_col)

def MoveHead():
	global size
	global current_head
	global candy
	global score
	global playing
	next_row = 0
	next_col = 0

	last_row = current_head_rows[current_head]
	last_col = current_head_cols[current_head]
	move = input()
	if move == 'a':
		if last_col - 1 >= 0:
			next_row = last_row
			next_col = last_col - 1
		else:
			playing = False
			return
	elif move == 'd':
		if last_col + 1 < size:
			next_row = last_row
			next_col = last_col + 1
		else:
			playing = False
			return
	elif move == 'w':
		if last_row - 1 >= 0:
			next_row = last_row - 1
			next_col = last_col
		else:
			playing = False
			return
	elif move == 's':
		if last_row + 1 < size:
			next_row = last_row + 1
			next_col = last_col
		else:
			playing = False
			return
	else:
		playing = False
		return

	if board[next_row][next_col] == '*':
		score += 1
		candy = False
	elif board[next_row][next_col] == '#':
		playing = False
		return

	board[next_row][next_col] = '@'
	board[last_row][last_col] = '#'
	current_head_rows.append(next_row)
	current_head_cols.append(next_col)
	current_head += 1

def MoveTail():
	global size
	global current_tail
	global candy
	global current_candy
	global candy_row_valid
	global candy_col_valid
	if current_head_rows[current_tail] == candy_rows[current_candy] and current_head_cols[current_tail] == candy_cols[current_candy]:
		current_candy += 1
	else:	
		board[current_head_rows[current_tail]][current_head_cols[current_tail]] = ' '
		current_tail += 1
		board[current_head_rows[current_tail]][current_head_cols[current_tail]] = '#'

def MakeCandy():
	global size
	global candy
	candy_row = random.randint(0, size - 1)
	candy_col = random.randint(0, size - 1)

	if board[candy_row][candy_col] == ' ':
		board[candy_row][candy_col] = '*'
		candy_rows.append(candy_row)
		candy_cols.append(candy_col)
		candy = True

def ClearScreen():
	for i in range(0,50):
		print()

StartingPosition()
ClearScreen()
PrintBoard()

while playing:
	if candy == False:
		MakeCandy()
		ClearScreen()
		PrintBoard()
	MoveHead()
	MoveTail()
	ClearScreen()
	PrintBoard()

print("GAME OVER\nSCORE: {}".format(score))