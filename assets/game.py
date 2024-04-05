# pygame setup
import pygame
from random import randint
import sys


def basic_Game(p_gamemode=1):
    # Initialisation de pygame
    pygame.init()

    # Résolution de l'écran
    resolution = (0, 0)  # Utilise la résolution de l'écran principal

    # Couleurs
    BLANC = (255, 255, 255)
    NOIR = (0, 0, 0)
    ROUGE = (255, 0, 0)
    VERT = (0, 255, 0)
    BLEU = (0, 0, 255)

    # Création de la fenêtre du jeu en plein écran
    fenetre = pygame.display.set_mode(resolution, pygame.FULLSCREEN)
    largeur, hauteur = fenetre.get_size()
    c_largeur, c_hauteur = largeur // 2, hauteur // 2

    # Boucle principale du jeu
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Vérifie si un bouton a été cliqué
                if bouton_1.collidepoint(event.pos):
                    print("Bouton 1 cliqué !")
                elif bouton_2.collidepoint(event.pos):
                    print("Bouton 2 cliqué !")
                elif bouton_3.collidepoint(event.pos):
                    print("Bouton 3 cliqué !")
                elif bouton_4.collidepoint(event.pos):
                    print("Bouton 4 cliqué !")

        # Dessine les boutons
        bouton_1 = pygame.draw.rect(fenetre, ROUGE, (c_largeur // 4, c_hauteur // 4, c_largeur // 2, c_hauteur // 4))
        bouton_2 = pygame.draw.rect(fenetre, VERT, (c_largeur // 4, c_hauteur // 2, c_largeur // 2, c_hauteur // 4))
        bouton_3 = pygame.draw.rect(fenetre, BLEU, (c_largeur // 4, c_hauteur // 4 * 3, c_largeur // 2, c_hauteur // 4))
        bouton_4 = pygame.draw.rect(fenetre, BLANC, (c_largeur // 4, c_hauteur // 4, c_largeur // 2, c_hauteur // 4))

        # Met à jour l'affichage
        pygame.display.flip()