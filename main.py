


                # 1st Part # Who's playing ? (with 2 players) Welcoming ! #

# To start, i introduce the game and let my players choose their "side"

print(" Tic-Tac-Toe ")
playerX=input("Qui sera les X ?")                    # determine  players with input
print(f"{playerX}, Tu joueras avec les X !")
                                                     #each player choose between X and O
playerO=input("Qui sera les O ?")
print(f"{playerO}, Tu joueras avec les O !")

print(f"À vous de jouer {playerX} & {playerO}!")      #ready to play



                # 2 nd Part # Creating my functional playing Board ! #


def board(cases):                                      # Function board
    top = "-" * (3*4 + 1)                              #top line = "- "*width*4(space)+ 1for each "box"
    for i in (0, 3, 6):                                #doing loop 3 times from 0,3 and 6
        print(top)
        print(f"| {cases[i]} | {cases[i+1]} | {cases[i+2]} |")
    print(top)
number = ["1","2","3","4","5","6","7","8","9"]          #give number to my boxes

board(number)


# je definis mes combos gagnants
#je definis mes tours qui jooue a chaque tour  impair et pair + mes conditions


game=True #mon jeu par defaut vrai continue
turn=1

while turn<=9 and game==True:   #
  if turn % 2 ==1:                      #tour impair alors mon player O joue
    print(f"{playerO} à ton tour !")
    name_player= playerO
    symbole="O"

  elif turn % 2==0:                     # tour pair c est mon player X
    print(f"{playerX} à ton tour !")
    name_player=playerX
    symbole="X"


  choice=int(input("Choisis ta case :")) # je definis le choix du joueur pour qu il soit bien compris dans ma grille
  while True:
    if choice not in range (1, 10):
      print(" Entrée invalide, choisis une case (1-9) : ")    #je cree une boucle qui se repete jusqu a ce que ma donnee soit correcte
      choice= int(input("Entre une donnée valide (1-9): "))
    else:
      break


  position = int(choice)-1 #1 puisque python compte de 0 à 8
  if number[position] in ("X", "O"):
    print("Case déjà prise")

  number[position] = symbole

  board(number)
  turn+=1

  combo= [(0,1,2), (3,4,5),(6,7,8),(0,3,6), (1,4,7), (2,5,8),(0,4,8), (2,4,6)] # mais combi gagnate


  for a,b,c in combo:
    if number[a]==number[b]==number[c]==symbole:
      print(f"Bravo {name_player}")
      game=False
      break
    if game:
      break




