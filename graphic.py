import pygame
import random

# pygame.init


# screen=pygame.display.set_mode((300,300))


# pygame.quit
# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
#-----------------------------SCREEN SIZE---------------------#
LARGEUR = 600
HAUTEUR = 600
COULEUR_ARRIERE_PLAN = (40, 40, 40)
COULEUR_LIGNE = (70, 70, 70)
TAILLE_CELLULE = LARGEUR // 3
win = pygame.display.set_mode((LARGEUR, HAUTEUR))

pygame.display.set_caption("Morpion")

#-----------------------------Players-------------------------#

SYMBOLE_JOUEUR = "X"
SYMBOLE_IA = "O"
COULEUR_JOUEUR = (0, 255, 0)
COULEUR_IA = (255, 0, 0)
COULEUR_VIDE = (0, 0, 0)


#----------------------------Main rules---------------------#

plateau = [["" for _ in range(3)] for _ in range(3)]
tour = "joueur"
partie_terminee = False
vainqueur = None




#----------------------------Button-------------------------#

LARGEUR_BOUTON = 200
HAUTEUR_BOUTON = 50
COULEUR_BOUTON = (50, 50, 50)
COULEUR_TEXTE_BOUTON = (255, 255, 255)
POLICE_BOUTON = pygame.font.Font(None, 30)

reset_button_rect = pygame.Rect(
    (LARGEUR - LARGEUR_BOUTON) // 2,
    (HAUTEUR - HAUTEUR_BOUTON) // 2,
    LARGEUR_BOUTON,
    HAUTEUR_BOUTON,
)

#----------------------------Function-------------------------#
## Fonctions d'aide
name_player= playerX
name_player=playerO
# board:
def board(cases):
    top = "-" * (3*4 + 1)
    for i in (0, 3, 6):
        print(top)
        print(f"| {cases[i]} | {cases[i+1]} | {cases[i+2]} |")
    print(top)

number = ["1","2","3","4","5","6","7","8","9"]

# combo:
combo = [
    (0,1,2), (3,4,5), (6,7,8),
    (0,3,6), (1,4,7), (2,5,8),
    (0,4,8), (2,4,6),
]

# full board:
def full_board(map):
    # True si toutes les cases contiennent "X" ou "O"
    return all(c in ("X", "O") for c in map)

# winer :
def winner(map, symbol):
    for a, b, c in combo:
        if [a] == symbol and map[b] == symbol and map[c] == symbol:
            return True
    return False

# --- Jouer un coup avec coordonnées (x,y) 0..2 ---
def faire_coup(map, x, y, symbole):                             #x = line , y = column
    # bornes correctes : ET, pas OU
    if not (0 <= x <= 2 and 0 <= y <= 2):
        return False
    i = y * 3 + x
    # case déjà occupée ?
    if map[i] in ("X", "O"):
        return False
    map[i] = symbole
    return True





    ## Effectuer un coup sur le plateau de jeu
    pass


def vérifier_fin_partie():
    ## Vérifier si la partie est terminée
    pass

def player_win(number, symbole):

      print(f"Bravo {name_player} tu as gagné !")                                # true if winning
      game = False   ## Dessiner le message du gagnant sur la fenêtre
    pass

#def dessiner_bouton_reset():
    ## Dessiner le bouton de réinitialisation sur la fenêtre
    pass

#def réinitialiser_partie():
    ## Réinitialiser l'état de la partie
    pass


pygame.quit()



