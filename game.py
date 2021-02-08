import pygame
from block import Block
from random import choice, randint

class Game:
    def __init__(self):

        # initialiser
        self.tableau = [['*' for i in range(4)] for j in range(4)]
        self.begin = [2] * 9 + [4] * 1

        self.direction = {'left': [],
                        'right': [],
                        'up': [],
                        'down': []}
    def reset(self):
        for i in range(4):
            for j in range(4):
                if self.tableau[i][j] != "*":
                    self.tableau[i][j].fusion = True

    def new_block(self):
        '''
        This module place a new block in the game.
        '''
        while True:
            x, y = randint(0, 3),randint(0, 3)
            
            if self.tableau[x][y] == '*':
                number = choice(self.begin)
                self.tableau[x][y] = Block(number, 150 * y + 3, 150 * x + 103)
                break

    def move(self, direction):
        mouvement = False

        for i in range(4):
            for j in range(4):
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
                    
        
        return mouvement
    
    def check(self):
        '''
        This module check if the game is over.

        return bool: False the game is not over; True the game is over
        '''

        # Check that they are still blank case
        for i in range(len(self.tableau)):
            for j in range(len(self.tableau[i])):

                if self.tableau[i][j] == "*":
                    return True

        for i in range(len(self.tableau)):
            for j in range(len(self.tableau[i])):
                if j < 3 and self.tableau[i][j].number == self.tableau[i][j + 1].number:
                    return True 

                if i < 3 and self.tableau[i][j].number == self.tableau[i + 1][j].number:
                    return True

        # The game is over
        return False