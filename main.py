


                # 1st Part # Who's playing ? (with 2 players) Welcoming ! #

#Introduce Game:


print(" Tic-Tac-Toe ")
playerX=input("Qui sera les X ?")                          # determine  players with input
print(f"{playerX}, Tu joueras avec les X !")
                                                           #each player choose between X and O
playerO=input("Qui sera les O ?")
print(f"{playerO}, Tu joueras avec les O !")

print(f"À vous de jouer {playerX} & {playerO}!")           #ready to play



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





                #3 rd Part # I define my turns, and conditions  #


game=True                                                     # true by default, as long as the game is true is running
turn=1                                                        # turn counter start from 1

# Turn :

while turn<=9 and game==True:                                 #stop after 9 turns or if game become false
  if turn % 2 ==1:                                            #if odd turn player O play
    print(f"{playerO} à ton tour !")
    name_player= playerO
    symbol="O"


  if turn % 2==0:                                             # if even turn player X play
    print(f"{playerX} à ton tour !")
    name_player=playerX
    symbol="X"

  #Conditions:
                                                              # player X start to play
  choice=int(input("Choisis ta case :"))                      # input for choosing a cell in board
  while True:
    if choice not in range (1, 10):                           #make sure player choose a good cell
      print(" Entrée invalide, choisis une case (1-9) : ")
      choice= int(input("Entre une donnée valide (1-9): "))   #loop is running until players select a good cells
    else:
      break                                                   # break to get out the loop


  position = int(choice)-1                                    # convert in 1 to 9 because python count from 0 to 8
  if number[position] in ("X", "O"):                          # cells is already occupied
    print("Case déjà prise")

  number[position] = symbol                                   # for printing symbols instead numbers

  board(number)                                               # call my board
  turn+=1                                                     # game run +1 if all conditions are respected



  #Winner positions:


  combo= [(0,1,2), (3,4,5),(6,7,8),(0,3,6), (1,4,7), (2,5,8),(0,4,8), (2,4,6)]  # all possibilities for winning

  def winner(board, symbol):                                                     # function to call in my loop
    for a, b, c in combo:                                                        #a, b, c going trough my loop
      if board[a] == symbol and board[b] == symbol and board[c] == symbol:       # check if 3 x cells get "X" "0" in line or column
       return True                                                               # found a winning line of X or O
      return False                                                               # if no winning combination is found the game continues

  if winner(number, symbol):                                                     #call board & symbol
      print(f"Bravo {name_player} tu as gagné !")                                # true if winning
      game = False                                                               #and stop game

  elif game and turn >= 10:                                                        #if game turn to 10
     print("Match nul !")                                                        #no winners
     game = False                                                                #end game
