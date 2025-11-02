     # 2 nd Part # Creating my functional playing Board ! #
# Board:

def board(cases):                                           # Function board
    top = "-" * (3*4 + 1)                                   #top line = "- "*width*4(space)+ 1for each cells
    for i in (0, 3, 6):                                     #doing loop 3 times from 0,3 and 6
        print(top)
        print(f"| {cases[i]} | {cases[i+1]} | {cases[i+2]} |")
    print(top)
number = ["1","2","3","4","5","6","7","8","9"]               #give number to my cells

board(number)

#Winner positions:


combo= [(0,1,2), (3,4,5),(6,7,8),
          (0,3,6), (1,4,7), (2,5,8),
          (0,4,8), (2,4,6)]  # all possibilities for winning

def winner(board, symbol):                                                     # function to call in my loop
  for a, b, c in combo:                                                        #a, b, c going trough my loop
      if board[a] == symbol and board[b] == symbol and board[c] == symbol:       # check if 3 x cells get "X" "0" in line or column
       return True                                                               # found a winning line of X or O
    return False                                                               # if no winning combination is found the game continues

    if winner(number, symbol):                                                     #call board & symbol
      print(f"Bravo {name_player} tu as gagné !")                                # true if winning
      game = False                                                               #and stop game

   elif game and turn >9:                                                        #if game turn to 10
     print("Match nul !")                                                        #no winners
     game = False                                                                #end game
