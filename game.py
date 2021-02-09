import pygame
from block import Block
from random import choice, randint

class Game:
    def __init__(self):

        # initialiser
        self.tableau = [['*' for i in range(4)] for j in range(4)]
        self.begin = [2] * 9 + [4] * 1

        self.direction = {'left': [lambda i: i, lambda c: c > 0, lambda *args: (args[1], args[0])],
                        'right': [lambda i: 4 - (i + 1), lambda c: c < 3, lambda *args: (args[1], args[0])],
                        'up': [lambda i: i, lambda c: c > 0, lambda *args: args],
                        'down': [lambda i: 4 - (i + 1), lambda c: c < 3, lambda *args: args]}
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
                c = self.direction[direction][0](i)

                t = self.direction[direction][2](c, j)

                if self.direction[direction][1](i) and self.tableau[t[0]][t[1]] != "*":
                    # Devant c'est vide
                    if self.tableau[c + 1][j] == "*":
                        mouvement, happen = True, 1

                        # Arriver a la bonne place
                        if self.tableau[c][j].rect.y >= 150 * (c + 1) + 103:
                            self.tableau[c + 1][j] = self.tableau[c][j]
                            self.tableau[c][j] = "*"
                        else:
                            self.tableau[c][j].rect.y += 15

                    # Pour fussioner de nombre
                    elif self.tableau[c][j].number == self.tableau[c + 1][j].number and self.tableau[c][j].fusion == True and self.tableau[c + 1][j].fusion == True:
                        mouvement, happen = True, 1

                        if self.tableau[c][j].rect.y >= self.tableau[c + 1][j].rect.y:
                            self.tableau[c][j] = "*"
                            self.tableau[c + 1][j].change_image(self.tableau[c + 1][j].number * 2)
                            self.tableau[c + 1][j].fusion = False
                        else:
                            self.tableau[c][j].rect.y += 15
        
        
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