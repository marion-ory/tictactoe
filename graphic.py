import pygame #importation
pygame.init() #initialisation

screen = pygame.display.set_mode((400,400)) #ouvre une fenetre

running=True #jeu avance

while running:
  for event in pygame.event.get():
    if event.type==pygame.QUIT:
      running=False                     # rendre plus joli le terminal sur internet check



 #----------evenement Fermeture---------#

 #bouton fermeture recuperer à  chaque tour de boucle du jeu la liste des evenement







  pygame.quit()

