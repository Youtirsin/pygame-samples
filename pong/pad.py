import pygame

# config
PAD_SPD = 3


class Pad(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 80))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.spd = PAD_SPD

    def update(self):
        pass
