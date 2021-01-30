import pygame

# obstacle config
OB_WIDTH = 30
PLACE_X = 600
OB_BOTTOM = 300
OB_SPD = 4


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((OB_WIDTH, height))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect(bottom = OB_BOTTOM)

    def update(self):
        if self.rect.right >= 0:
            self.rect.right -= OB_SPD
        else:
            self.rect.left = PLACE_X
