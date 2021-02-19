import pygame

# config


class Pad(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 80))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()

    def update(self):
        pass
