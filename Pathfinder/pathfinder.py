import random

size = 10
obstacles = 15

goal_row = -1
goal_col = -1
start_row = -1
start_col = -1

empty = ' '
goal = '@'

moves_counter = 0
moves_rows = []
moves_cols = []

caught = False
over = False
moved = False
used = False

board = [[empty]*size for i in range(size)]

def PrintBoard():
	global size
	for i in range(0,size):
		for j in range(0,size - 1):
			print(board[i][j], end=' ')
		print(board[i][size - 1])

def MakeGoal():
	global size
	global goal_row
	global goal_col
	global goal
	goal_row = random.randint(0, size - 1)
	goal_col = random.randint(0, size - 1)
	board[goal_row][goal_col] = goal

def MakeStart():
	global size
	global start_row
	global start_col
	valid_pos = False

	while not valid_pos:
		start_row = random.randint(0, size - 1)
		start_col = random.randint(0, size - 1)
		if board[start_row][start_col] == empty:
			board[start_row][start_col] = '^'
			moves_rows.append(start_row)
			moves_cols.append(start_col)
			valid_pos = True

def MakeObstacle():
	global size
	valid_pos = False

	while not valid_pos:
		obs_row = random.randint(0, size - 1)
		obs_col = random.randint(0, size - 1)
		if board[obs_row][obs_col] == empty:
			board[obs_row][obs_col] = 'o'
			valid_pos = True
def Chase():
	global goal_row
	global goal_col
	global start_row
	global start_col
	global moves_counter
	global caught
	global over
	global moved
	global used
	next_start_col = -1
	next_start_row = -1

	moved = False
	used = False

	if start_row == goal_row and start_col == goal_col:
		print('GOT IT IN {} MOVES'.format(moves_counter))
		caught = True

	move_right = [moves_rows[moves_counter],moves_cols[moves_counter] + 1]
	diff_right = abs(goal_row - move_right[0]) + abs(goal_col - move_right[1])
	move_left = [moves_rows[moves_counter],moves_cols[moves_counter] - 1]
	diff_left = abs(goal_row - move_left[0]) + abs(goal_col - move_left[1])
	move_down = [moves_rows[moves_counter] + 1,moves_cols[moves_counter]]
	diff_down = abs(goal_row - move_down[0]) + abs(goal_col - move_down[1])
	move_up = [moves_rows[moves_counter] - 1,moves_cols[moves_counter]]
	diff_up = abs(goal_row - move_up[0]) + abs(goal_col - move_up[1])

	diffs = [diff_right, diff_left, diff_down, diff_up]
	diffs.sort()

	last_r = False
	last_l = False
	last_d = False
	last_u = False

	attempt = 0

	while not moved and attempt < 4:

		if diffs[attempt] == diff_right and start_col + 1 != size and not last_r:
			last_r = True
			next_start_col = start_col + 1
			next_start_row = start_row
			Validate(next_start_row,next_start_col)

		elif diffs[attempt] == diff_left and start_col - 1 >= 0 and not last_l:
			last_l = True
			next_start_col = start_col - 1
			next_start_row = start_row
			Validate(next_start_row,next_start_col)

		elif diffs[attempt] == diff_down and start_row + 1 != size and not last_d:
			last_d = True
			next_start_col = start_col
			next_start_row = start_row + 1
			Validate(next_start_row,next_start_col)

		elif diffs[attempt] == diff_up and start_row - 1 >= 0 and not last_u:
			last_u = True
			next_start_col = start_col
			next_start_row = start_row - 1
			Validate(next_start_row,next_start_col)

		attempt += 1

	if not moved and attempt == 4:
		over = True
		return

def Validate(next_start_row,next_start_col):
	next_row = next_start_row
	next_col = next_start_col
	global moves_counter
	global used
	global moved
	global start_row
	global start_col

	used = False
	moved = False

	if board[next_row][next_col] == empty or board[next_row][next_col] == goal:
		for i in range(0,moves_counter + 1):
			if next_col == moves_cols[i] and next_row == moves_rows[i]:
				used = True
		if not used:
			moved = True
			moves_counter += 1
			if board[next_row][next_col] != goal:
				board[next_row][next_col] = '.'
			start_row = next_row
			start_col = next_col
			moves_rows.append(start_row)
			moves_cols.append(start_col)

MakeGoal()
MakeStart()
for i in range(0, obstacles):
	MakeObstacle()
print()
PrintBoard()

while not caught:
	Chase()
	if not caught:
		print()
		print("------------------------------")
		print()
		PrintBoard()
	if over == True:
		print("GAME OVER")
		break
