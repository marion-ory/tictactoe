import random

            #---------------IA play random in Titactoe -------------#


               # 1st Part # Who's playing ? (with 2 players) Welcoming ! #

#Introduce Game:
#
# import et variable global en 1
# definition fonctions
# code general

                                                                     # Real Player play with O
player_O = input("Qui sera les O ?")
print(f"{player_O}, Tu joueras avec les O !")

print(f"À vous de jouer {player_O} !")                                 #ready to play



                # 2 nd Part # Creating my functional playing Board ! #
# Board:

number = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]                        #give number to my cells

game = True                                                           # true by default, as long as the game is true is running
turn = 1                                                              # turn counter start from 1


combo = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)
]  # all possibilities for winning


def board(cases):                                                     # Function board
    top = "-" * (3 * 4 + 1)                                             #top line = "- "*width*4(space)+ 1for each cells
    for i in (0, 3, 6):                                               #doing loop 3 times from 0,3 and 6
        print(top)
        print(f"| {cases[i]} | {cases[i+1]} | {cases[i+2]} |")
    print(top)


def board_ia(cases, signe):
    if signe not in ("X", "O"):                                     #return IA position (0,8)
        return False                                                # sign is not valid

    libres = [i for i in range(9) if cases[i] not in ("X", "O")]    # IA choosing free cell
    if not libres:
        return False                                                # no more free cell
    position = random.choice(libres)
    return position                                                 #sending position


def winner(board, symbol):                                                           # function to call in my loop
    for a, b, c in combo:                                                              #a, b, c going trough my loop
        if board[a] == symbol and board[b] == symbol and board[c] == symbol:             # check if 3 x cells get "X" "0" in line or column
            return True                                                                     # found a winning line of X or O
    return False                                                                       # if no winning combination is found the game continues


board(number)


                #3 rd Part # I define my turns, and conditions  #


# Turn :

while turn <= 9 and game == True:                                        #stop after 9 turns or if game become false
    if turn % 2 == 1:                                                   #if odd turn player O play
        print(f"{player_O} à ton tour !")
        name_player = player_O
        symbol = "O"


    if turn % 2 == 0:                                                    # if even turn  IA is playing
        name_player = "ia"
        symbol = "X"
        position = board_ia(number, symbol)
        if position is False:
            print("Erreur")                                              #error message if board is full
            game = False                                                  # end of game
            break                                                         #get out game
        print(f"IA joue : {position + 1}")

    #Conditions:
    # player X start to play
    if turn % 2 == 1:                                                   # if it's the human player's turn
        while True:                                                     # ask until a valid move
            try:
                choice = int(input("Choisis ta case :"))
            except ValueError:
                print(" Entrée invalide, choisis une case (1-9) : ")
                continue
            if choice not in range(1, 10):                             #make sure player choose a good cell
                print(" Entrée invalide, choisis une case (1-9) : ")
                continue

            position = int(choice) - 1                                   # convert in 1 to 9 because python count from 0 to 8

            if number[position] in ("X", "O"):
                print("Déja occupé, choisis une autre case (1-9)")
                continue
            break                                                        # break to get out the loop

    if turn % 2 == 0:                                                    # if it's IA's turn
        pass                                                             # IA already played using board_ia()


    number[position] = symbol                                          # for printing symbols instead numbers

    board(number)                                                      # call my board
    turn += 1                                                            # game run +1 if all conditions are respected

    if winner(number, symbol):                                                           #call board & symbol
        print(f"Bravo {name_player} tu as gagné !")                                      # true if winning
        game = False                                                                     #and stop game
        break

if game and turn > 9:                                                                   #if game turn to 10
    print("Match nul !")                                                                 #no winners
    game = False                                                                         #end game
import random

            #---------------IA play random in Titactoe -------------#



               # 1st Part # Who's playing ? (with 2 players) Welcoming ! #

#Introduce Game:
#
# import et variable global en 1
# definition fonctions
# code general
                                                                     # Real Player play with O
player_O=input("Qui sera les O ?")
print(f"{player_O}, Tu joueras avec les O !")

print(f"À vous de jouer {player_O} !")                                 #ready to play



                # 2 nd Part # Creating my functional playing Board ! #
# Board:

def board(cases):                                                     # Function board
    top = "-" * (3*4 + 1)                                             #top line = "- "*width*4(space)+ 1for each cells
    for i in (0, 3, 6):                                               #doing loop 3 times from 0,3 and 6
        print(top)
        print(f"| {cases[i]} | {cases[i+1]} | {cases[i+2]} |")
    print(top)
number = ["1","2","3","4","5","6","7","8","9"]                        #give number to my cells

board(number)





                #3 rd Part # I define my turns, and conditions  #


game=True                                                           # true by default, as long as the game is true is running
turn=1                                                              # turn counter start from 1


# ---- IA function :---#

def board_ia(cases, signe):
    if signe not in ("X", "O"):                                     #return IA position (0,8)
        return False                                                # sign is not valid

    libres = [i for i in range(9) if cases[i] not in ("X", "O")]    # IA choosing free cell
    if not libres:
        return False                                                # no more free cell
    position = random.choice(libres)
    return position                                                 #sending position


# Turn :

while turn<=9 and game==True:                                        #stop after 9 turns or if game become false
  if turn % 2 ==1:                                                   #if odd turn player O play
    print(f"{player_O} à ton tour !")
    name_player= player_O
    symbol="O"


  if turn % 2==0:                                                    # if even turn  IA is playing
    name_player = "ia"
    symbol = "X"
    position = board_ia(number, symbol)
    if position is False:
        print("Erreur")                                              #error message if board is full
        game = False                                                  # end of game
        break                                                         #get out game
    print(f"IA joue : {position + 1}")

  #Conditions:
                                                                       # player X start to play
  if turn % 2 == 1:                                                   # if it's the human player's turn
      while True:                                                     # ask until a valid move
          choice=int(input("Choisis ta case :"))
          if choice not in range (1, 10):                             #make sure player choose a good cell
              print(" Entrée invalide, choisis une case (1-9) : ")
              continue

          position = int(choice)-1                                   # convert in 1 to 9 because python count from 0 to 8

          if number[position] in ("X", "O"):
              print("Déja occupé, choisis une autre case (1-9)")
              continue
          break                                                        # break to get out the loop

  if turn % 2 == 0:                                                    # if it's IA's turn
      pass                                                             # IA already played using board_ia()


  number[position] = symbol                                          # for printing symbols instead numbers

  board(number)                                                      # call my board
  turn+=1                                                            # game run +1 if all conditions are respected



  #Winner positions:


  combo= [(0,1,2), (3,4,5),(6,7,8),
          (0,3,6), (1,4,7), (2,5,8),
          (0,4,8), (2,4,6)]                                                            # all possibilities for winning

  def winner(board, symbol):                                                           # function to call in my loop
    for a, b, c in combo:                                                              #a, b, c going trough my loop
      if board[a] == symbol and board[b] == symbol and board[c] == symbol:             # check if 3 x cells get "X" "0" in line or column
       return True                                                                     # found a winning line of X or O
    return False                                                                       # if no winning combination is found the game continues

  if winner(number, symbol):                                                           #call board & symbol
      print(f"Bravo {name_player} tu as gagné !")                                      # true if winning
      game = False                                                                     #and stop game

if game and turn >9:                                                                   #if game turn to 10
  print("Match nul !")                                                                 #no winners
  game = False                                                                         #end game
