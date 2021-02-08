import pygame

class Block(pygame.sprite.Sprite):
    def __init__(self, number, x, y):
        super().__init__()
        self.number = number
        self.image = pygame.image.load('assets/blocks/'+ str(number) +'.png')
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.fusion = True
    
    def change_image(self, new):
        self.number = new
        self.image = pygame.image.load(f'assets/blocks/{new}.png')
    
    def change_coordonnee(self, x, y):
        self.rect.x, self.rect.y = x, y
    
    def deplace(self, direction):
        pass