# Fore : change background color

# Back : change color

# Style : bright writing


from colorama import init, Fore, Style, Back
init(autoreset=True)                                                                                          # ← reset after each print



                # 1st Part # Who's playing ? (with 2 players) Welcoming ! #

#Introduce Game:


print(Back.LIGHTGREEN_EX + Fore.WHITE + "\n" * 4  +  "      ✖️ ✖️ ✖️    𝓣  I  C   -   T  ⓐ  C   -   T  🅾️  E    ✖️ ✖️ ✖️        "+ "\n" * 4)



player_X=input("\n" * 4 + Fore.CYAN + Style.BRIGHT+ "👤 Qui sera les X ?  ")                                                    # determine  players with input
print(Back.LIGHTWHITE_EX+Fore.BLACK + Style.BRIGHT + "\n" *1 + '\033[20C' + \
      f"  {player_X} , Tu joueras avec les ✖️ !  ")                                                                            #each player choose between X and O

player_O=input(Fore.GREEN + "\n" *1 +"👤 Qui sera les O ?  ")
print(Back.LIGHTWHITE_EX+Fore.BLACK +Style.BRIGHT + "\n" *1 + '\033[20C' + \
      f"  {player_O}, Tu joueras avec les 🅾️ !  ")

print("\n" * 3 +Back.LIGHTWHITE_EX+Fore.MAGENTA +'\033[10C' + \
      f"  🏁   À vous de jouer {player_X} & {player_O}  !    🏁  ")        #ready to play # "\n" * 3 = Line # '\033[10C' =space character



                # 2 nd Part # Creating my functional playing Board ! #
# Board:

sep=Fore.BLACK                                                                                                    # getting my "|" in black in my function
DISPLAY = {"X":"✖️", "O":"🅾️"}                                                                                    # saved emojis for X and O

def cell(a):                                                                                                      # function to allow color in my cell's board
  if a=="X":
    return( DISPLAY["X"] + sep)
  elif a=="O":
    return( DISPLAY["O"]+ sep)
  return Fore.RED + a +sep                                                                                       # return color for number in board

def board(cases):                                                                                                # Function board
    top = "-" * (3*8+ 1)                                                                                         #top line = "- "*width*4(space)+ 1for each cells
    for i in (0, 3, 6):                                                                                          #doing loop 3 times from 0,3 and 6
        print(Fore.BLACK + top)
        print(Fore.BLUE + f"{sep}|   {cell(cases[i])}   |   {cell(cases[i+1])}   |   {cell(cases[i+2])}   |")
    print(Fore.BLACK + top)
number = ["1","2","3","4","5","6","7","8","9"]               #give number to my cells

board(number)





                #3 rd Part # I define my turns, and conditions  #


game=True                                                                                                          # true by default, as long as the game is true is running
turn=1                                                                                                             # turn counter start from 1

# Turn :

while turn<=9 and game==True:                                                                                        #stop after 9 turns or if game become false
  if turn % 2 ==1:                                                                                                   #if odd turn player X play
    print("\n" * 2 + Back.LIGHTWHITE_EX+ Fore.CYAN + '\033[5C' \
          + f" {player_X} à ton tour ! ")
    name_player=player_X
    symbol="X"


  if turn % 2==0:                                                                                                    # if even turn player O play
    print("\n" * 2 + Back.LIGHTWHITE_EX + Fore.GREEN +'\033[5C'\
          + f" {player_O} à ton tour ! ")
    name_player= player_O
    symbol="O"

  #Conditions:
                                                                                                                    # player X start to play
  choice=int(input("\n" * 2  + "Choisis ta case : "))                                                               # input for choosing a cell in board
  while True:
    if choice not in range (1, 10):                                                                                 #make sure player choose a good cell
      print("\n" * 2 + " Entrée invalide, choisis une case (1-9) : ")
      choice= int(input("\n" * 2  + "Entre une donnée valide (1-9): "))                                             #loop is running until players select a good cells
    else:
      break                                                                                                          # break to get out the loop


  position = int(choice)-1                                                                                           # convert in 1 to 9 because python count from 0 to 8
  if number[position] in ("X", "O"):                                                                                 # cells is already occupied
    print("\n" * 2 + "Case déjà prise")
    continue                                                                                                         # going trough the loop

  number[position] = symbol                                                                                          # for printing symbols instead numbers

  board(number)                                                                                                      # call my board
  turn+=1                                                                                                            # game run +1 if all conditions are respected



  #Winner positions:


  combo= [(0,1,2), (3,4,5),(6,7,8),
          (0,3,6), (1,4,7), (2,5,8),
          (0,4,8), (2,4,6)]                                            # all possibilities for winning

  def winner(board, symbol):                                                                                              # function to call in my loop
    for a, b, c in combo:                                                                                                 #a, b, c going trough my loop
      if board[a] == symbol and board[b] == symbol and board[c] == symbol:                                                # check if 3 x cells get "X" "0" in line or column
       return True                                                                                                        # found a winning line of X or O
    return False                                                                                                          # if no winning combination is found the game continues

  if winner(number, symbol):                                                                                                        #call board & symbol
      print(Back.GREEN+ Fore.WHITE +  "\n" * 2 + '\033[40C' + \
        f" 🎉 Bravo {name_player} tu as gagné ! "+ "\n" * 2 )                                                                       # true if winning
      game = False                                                                                                                  #and stop game

  elif game and turn >9:                                                                                                            #if game turn to 10
     print(Back.MAGENTA + Fore.WHITE + "\n" * 2 + '\033[40C' + \
       " 🚩 Match nul ! 🚩 "+ "\n" * 2 )                                                                                             #no winners
     game = False                                                                                                                   #end game
