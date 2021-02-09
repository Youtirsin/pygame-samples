import pygame


class Ground(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((400, 5))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect(y=500)
