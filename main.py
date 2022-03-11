import random
def moves_allowed():
  left_allowed = False
  up_allowed = False
  down_allowed = False
  right_allowed = False
  for i in range(4):
    for j in range(4):
      if(board[i][j] == "*"):
        for x in range(4 - j):
          if(board[i][j + x] != "*"):
            left_allowed = True
        for x in range(j):
          if(board[i][j - x - 1] != "*"):
            right_allowed = True
        for x in range(4 - i):
          if(board[i + x][j] != "*"):
            up_allowed = True
        for x in range(i):
          if(board[i - x - 1][j] != "*"):
            down_allowed = True
      if(j < 3):  
        if(board[i][j] == board[i][j + 1] and board[i][j] != "*"):
          left_allowed = True
          right_allowed = True
      if(i < 3):
        if(board[i][j] == board[i + 1][j] and board[i][j] != "*"):
          up_allowed = True
          down_allowed = True
  return left_allowed, up_allowed, down_allowed, right_allowed

board = [["*", "*", "*", "*"], ["*", "*", "*", "*"], ["*", "*", "*", "*"], ["*", "*", "*", "*"]]
def game():
  start_one = random.randint(0, 15)
  start_two = random.randint(0, 15)
  if(start_two == start_one):
    while(start_two == start_one):
      start_two = random.randint(0, 15)
  board[int((start_one - (start_one % 4)) / 4)][start_one % 4] = 2
  board[int((start_two - (start_two % 4)) / 4)][start_two % 4] = 2
  end = False
  won = False
  while(not(end)):
    for i in board:
      toprint = []
      for j in i:
        toprint.append(f"|{j}|")
      print(toprint)
    direct = input("Which direction do you wish to move everything; Left (1), Up (2), Down (3), or Right (4)?")
    if(not((direct == "1" and moves_allowed()[0]) or (direct == "2" and moves_allowed()[1]) or (direct == "3" and moves_allowed()[2]) or (direct == "4" and moves_allowed()[3]))):
      while(not((direct == "1" and moves_allowed()[0]) or (direct == "2" and moves_allowed()[1]) or (direct == "3" and moves_allowed()[2]) or (direct == "4" and moves_allowed()[3]))):
        direct = input("Please input 1, 2, 3, or 4, to select a direction in which it is possible to move. Which direction do you wish to move everything; Left (1), Up (2), Down (3), or Right (4)?")
    if(direct == "1"):
      for i in range(4):
        for j in range(3):
          if(board[i][j] == "*"):
            cont = False
            for x in range(4 - j):
              if(board[i][j + x] != "*"):
                cont = True
            if(cont):
              while(board[i][j] == "*"):
                board[i][j] = board[i][j + 1]
                for x in range(3 - j):
                  board[i][j + x] = board[i][j + x + 1]
                board[i][3] = "*"
      for i in range(4):
        for j in range(3):
          if(board[i][j] == board[i][j + 1] and board[i][j] != "*"):
            board[i][j + 1] *= 2
            for x in range(3 - j):
              board[i][j + x] = board[i][j + x + 1]
            board[i][3] = "*"
    elif(direct == "4"):
      for i in range(4):
        for j in range(3):
          if(board[i][3 - j] == "*"):
            cont = False
            for x in range(4 - j):
              if(board[i][3 - j - x] != "*"):
                cont = True
            if(cont):
              while(board[i][3 - j] == "*"):
                board[i][3 - j] = board[i][2 - j]
                for x in range(3 - j):
                  board[i][3 - j - x] = board[i][2 - j - x]
                board[i][0] = "*"
      for i in range(4):
        for j in range(3):
          if(board[i][3 - j] == board[i][2 - j] and board[i][3 - j] != "*"):
            board[i][2 - j] *= 2
            for x in range(3 - j):
              board[i][3 - j - x] = board[i][2 - j - x]
            board[i][0] = "*"
    elif(direct == "2"):
      for i in range(4):
        for j in range(3):
          if(board[j][i] == "*"):
            cont = False
            for x in range(4 - j):
              if(board[j + x][i] != "*"):
                cont = True
            if(cont):
              while(board[j][i] == "*"):
                board[j][i] = board[j + 1][i]
                for x in range(3 - j):
                  board[j + x][i] = board[j + x + 1][i]
                board[3][i] = "*"
      for i in range(4):
        for j in range(3):
          if(board[j][i] == board[j + 1][i] and board[j][i] != "*"):
            board[j + 1][i] *= 2
            for x in range(3 - j):
              board[j + x][i] = board[j + x + 1][i]
            board[3][i] = "*"
    else:
      for i in range(4):
        for j in range(3):
          if(board[3 - j][i] == "*"):
            cont = False
            for x in range(4 - j):
              if(board[3 - j - x][i] != "*"):
                cont = True
            if(cont):
              while(board[3 - j][i] == "*"):
                board[3 - j][i] = board[2 - j][i]
                for x in range(3 - j):
                  board[3 - j - x][i] = board[2 - j - x][i]
                board[0][i] = "*"
      for i in range(4):
        for j in range(3):
          if(board[3 - j][i] == board[2 - j][i] and board[3 - j][i] != "*"):
            board[2 - j][i] *= 2
            for x in range(3 - j):
              board[3 - j - x][i] = board[2 - j - x][i]
            board[0][i] = "*"
    new_two = random.randint(0,15)
    if(board[int((new_two - (new_two % 4)) / 4)][new_two % 4] != "*"):
      while(board[int((new_two - (new_two % 4)) / 4)][new_two % 4] != "*"):
          new_two = random.randint(0,15)
    board[int((new_two - (new_two % 4)) / 4)][new_two % 4] = 2
    if(not(moves_allowed()[0] or moves_allowed()[1] or moves_allowed()[2] or moves_allowed()[3])):
      end = True
    for i in board:
      for j in i:
        if(j == 2048):
          won = True
          end = True
  for i in board:
    toprint = []
    for j in i:
      toprint.append(f"|{j}|")
    print(toprint)
  if(won):
    print("YOU WIN!")
  else:
    print("GAME OVER")