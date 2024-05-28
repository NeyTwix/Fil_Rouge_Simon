# pygame setup
try:
    import pygame, random, sys
except Exception as e:
    print(f"\n\n\033[91mModule pygame, sys or random Not Found\nPlease make sure you have installed all module before launching this file again.\n\n\033[0m")
    exit()

def basic_Game(p_gamemode=1):
    pygame.init()

    resolution, jaune, bleu, rouge, vert = (0, 0), (255, 255, 0), (0, 0, 255), (255, 0, 0), (0, 255, 0)
    fenetre=pygame.display.set_mode(resolution, pygame.FULLSCREEN)
    largeur, hauteur = fenetre.get_size()
    c_largeur, c_hauteur = largeur // 2, hauteur // 2
    
    while True:
        bouton_bleu = pygame.draw.rect(fenetre, bleu, (c_largeur, c_hauteur, c_largeur, c_hauteur))
        bouton_jaune = pygame.draw.rect(fenetre, jaune, (0, c_hauteur, c_largeur, c_hauteur))
        bouton_rouge = pygame.draw.rect(fenetre, rouge, (c_largeur, 0, c_largeur, c_hauteur))
        bouton_vert = pygame.draw.rect(fenetre, vert, (0, 0, c_largeur, c_hauteur))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if bouton_bleu.collidepoint(event.pos):
                    print("Bleu cliqué !")
                elif bouton_jaune.collidepoint(event.pos):
                    print("Jaune cliqué !")
                elif bouton_rouge.collidepoint(event.pos):
                    print("Rouge cliqué !")
                elif bouton_vert.collidepoint(event.pos):
                    print("Vert cliqué !")


        pygame.display.flip()

# DEBUG
basic_Game()