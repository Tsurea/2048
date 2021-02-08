"""
Blue lock c'est trop bien
"""
import pygame
from game import Game

def mettre_a_jour():
    # mettre le fond de l'ecran
    screen.blit(background, (0, 0))

    # mettre tous les blocs
    for i in range(len(game.tableau)):
        for j in range(len(game.tableau[i])):
            if game.tableau[i][j] != '*':
                screen.blit(game.tableau[i][j].image, (game.tableau[i][j].rect.x, game.tableau[i][j].rect.y))
    
    # mise à jour de l'ecran
    pygame.display.flip()

pygame.init()

# generer le jeu
screen = pygame.display.set_mode((600, 700))
pygame.display.set_caption('2048')

clock = pygame.time.Clock()

# charger le fond
background = pygame.image.load('assets/bg.png')

# charger le jeu
game = Game()

# start the game
for i in range(2):
    game.new_block()

running = True

# boucle de jeu
while running and game.check():
    happen = 0

    for event in pygame.event.get():
        # Fermeture de la fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")

        # une touche du clavier a été pressé
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:

                mouvement = True

                while mouvement:
                    mouvement = False

                    for i in range(4):
                        for j in range(4):
                            # Si c'est pas nul

                            c = 4 - (i + 1)

                            if c < 3 and game.tableau[j][c] != "*":
                                # Devant c'est vide
                                if game.tableau[j][c + 1] == "*":
                                    mouvement, happen = True, 1

                                    # Arriver a la bonne place
                                    if game.tableau[j][c].rect.x >= 150 * (c + 1) + 3:
                                        game.tableau[j][c + 1] = game.tableau[j][c]
                                        game.tableau[j][c] = "*"
                                    else:
                                        game.tableau[j][c].rect.x += 15

                                # Pour fussioner de nombre
                                elif game.tableau[j][c].number == game.tableau[j][c + 1].number and game.tableau[j][c].fusion == True and game.tableau[j][c + 1].fusion == True:
                                    mouvement, happen = True, 1

                                    if game.tableau[j][c].rect.x >= game.tableau[j][c + 1].rect.x:
                                        game.tableau[j][c] = "*"
                                        game.tableau[j][c + 1].change_image(game.tableau[j][c + 1].number * 2)
                                        game.tableau[j][c + 1].fusion = False
                                    else:
                                        game.tableau[j][c].rect.x += 15
                    
                    mettre_a_jour()


            elif event.key == pygame.K_LEFT:
                
                mouvement = True

                while mouvement:
                    mouvement = False

                    for i in range(4):
                        for j in range(4):
                            # Si c'est pas nul

                            c = i

                            if c > 0 and game.tableau[j][c] != "*":
                                # Devant c'est vide
                                if game.tableau[j][c - 1] == "*":
                                    mouvement, happen = True, 1

                                    # Arriver a la bonne place
                                    if game.tableau[j][c].rect.x <= 150 * (c - 1) + 3:
                                        game.tableau[j][c - 1] = game.tableau[j][c]
                                        game.tableau[j][c] = "*"
                                    else:
                                        game.tableau[j][c].rect.x -= 15

                                # Pour fussioner de nombre
                                elif game.tableau[j][c].number == game.tableau[j][c - 1].number and game.tableau[j][c].fusion == True and game.tableau[j][c - 1].fusion == True:
                                    mouvement, happen = True, 1

                                    if game.tableau[j][c].rect.x <= game.tableau[j][c - 1].rect.x:
                                        game.tableau[j][c] = "*"
                                        game.tableau[j][c - 1].change_image(game.tableau[j][c - 1].number * 2)
                                        game.tableau[j][c - 1].fusion = False
                                    else:
                                        game.tableau[j][c].rect.x -= 15
                    
                    mettre_a_jour()
                    
            elif event.key == pygame.K_UP:
                mouvement = True

                while mouvement:
                    mouvement = False

                    for i in range(4):
                        for j in range(4):
                            # Si c'est pas nul

                            c = i

                            if c > 0 and game.tableau[c][j] != "*":
                                # Devant c'est vide
                                if game.tableau[c - 1][j] == "*":
                                    mouvement, happen = True, 1

                                    # Arriver a la bonne place
                                    if game.tableau[c][j].rect.y <= 150 * (c - 1) + 103:
                                        game.tableau[c - 1][j] = game.tableau[c][j]
                                        game.tableau[c][j] = "*"
                                    else:
                                        game.tableau[c][j].rect.y -= 15

                                # Pour fussioner de nombre
                                elif game.tableau[c][j].number == game.tableau[c - 1][j].number and game.tableau[c][j].fusion == True and game.tableau[c - 1][j].fusion == True:
                                    mouvement, happen = True, 1

                                    if game.tableau[c][j].rect.y <= game.tableau[c - 1][j].rect.y:
                                        game.tableau[c][j] = "*"
                                        game.tableau[c - 1][j].change_image(game.tableau[c - 1][j].number * 2)
                                        game.tableau[c - 1][j].fusion = False
                                    else:
                                        game.tableau[c][j].rect.y -= 15
                    
                    mettre_a_jour()
            elif event.key == pygame.K_DOWN:
                mouvement = True

                while mouvement:
                    mouvement = False

                    for i in range(4):
                        for j in range(4):
                            # Si c'est pas nul

                            c = 4 - (i + 1)

                            if c < 3 and game.tableau[c][j] != "*":
                                # Devant c'est vide
                                if game.tableau[c + 1][j] == "*":
                                    mouvement, happen = True, 1

                                    # Arriver a la bonne place
                                    if game.tableau[c][j].rect.y >= 150 * (c + 1) + 103:
                                        game.tableau[c + 1][j] = game.tableau[c][j]
                                        game.tableau[c][j] = "*"
                                    else:
                                        game.tableau[c][j].rect.y += 15

                                # Pour fussioner de nombre
                                elif game.tableau[c][j].number == game.tableau[c + 1][j].number and game.tableau[c][j].fusion == True and game.tableau[c + 1][j].fusion == True:
                                    mouvement, happen = True, 1

                                    if game.tableau[c][j].rect.y >= game.tableau[c + 1][j].rect.y:
                                        game.tableau[c][j] = "*"
                                        game.tableau[c + 1][j].change_image(game.tableau[c + 1][j].number * 2)
                                        game.tableau[c + 1][j].fusion = False
                                    else:
                                        game.tableau[c][j].rect.y += 15
                    
                    mettre_a_jour()
    if happen:
        game.reset()
        game.new_block()
    mettre_a_jour()

if not(game.check()):
    print('Tu as perdu')