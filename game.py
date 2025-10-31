import tkinter


def check_nul():
  print("Match nul")

def print_winner():
  global win
  if win is False:
    win = True

  print("Le joueur", current_player, "a gagné le jeu ")

def switch_player ():                                                  #tour de jeu current player X
  global current_player                                       # créer une variable globale en dehors d une fonction
  if current_player=="X":
    current_player="O"
  else:
    current_player="X"

def check_win(clicked_row, clicked_col):   # detecter victoire horizontal:
  count = 0
  for i in range(3):
    current_button = buttons[i][clicked_row]                      # <- balayer les colonnes sur la ligne cliquée
    if current_button['text'] == current_player:                  #si le boutton =X
      count += 1

  if count == 3:
    print_winner()
    return

  # detecter victoire vertical:
  count = 0
  for i in range(3):
    current_button = buttons[clicked_col][i]                      # <- balayer les lignes sur la colonne cliquée
    if current_button['text'] == current_player:                  #si le boutton =X
      count += 1

  if count == 3:
    print_winner()
    return

  #Detecter victoire diagonal:
  count = 0
  for i in range(3):
    current_button = buttons[i][i]                                # <- un seul cas:  00 11 22
    if current_button['text'] == current_player:
      count += 1

  if count == 3:
    print_winner()
    return

  #Detecter victoire diagonale inversé:
  count = 0
  for i in range(3):
    current_button = buttons[2 - i][i]                            #2-1=2  # <- un seul cas:  02 11 22 20
    if current_button['text'] == current_player:
      count += 1

  if count == 3:
    print_winner()
    return


  if win is False:
    count=0
    for col in range (3):
      for row in range (3):
        current_button=buttons[col][row]
        if current_button['text']=='X'or current_button['text']=='O':
          count+=1

        if count==9:
          print("Match nul")

  # -------------------------------------------------------

def place_symbol(row, column):                  # definir la place de mes bouttons dans les colonnes et les rangées
  print("click", row, column)

  clicked_button = buttons[column][row]

  if clicked_button["text"] == "":               #pour ne pas écraser un joueur existant.   # condition inverse
      clicked_button.config (text=current_player)

  check_win(row, column)
  switch_player()

def draw_grid():                          # créer un bouton qui appartient à la fenêtre root
  for column in range(3):                 # 3x par colonne
    buttons_in_cols = []                  # liste temporaire
    for row in range(3):                  # 3x par ligne
      button = tkinter.Button(            # créer un bouton qui appartient à la fenêtre root
        root,
        font=("Arial", 50),               # police
        width=5, height=3,                # dimension
        command=lambda r=row, c=column: place_symbol(r, c)  # rappel fonction de placement
      )
      button.grid(row=row, column=column)
      buttons_in_cols.append(button)
    buttons.append(buttons_in_cols)       # <-- DOIT être dans la boucle 'for column'

# ----------------- Stockage --------------------------- #
buttons = []  # 2 dimensions pour lignes et colonnes
current_player="X"
win=False
# ----------------- créer fenêtre du jeu ---------------- #
root = tkinter.Tk()       # main window
root.title(" Tic Tac Toe Game ")  # defining name of window
root.minsize(500, 500)    # size window

draw_grid()
root.mainloop()
