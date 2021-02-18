import pygame


class Border(pygame.sprite.Sprite):
    def __init__(self, collide_type, length):
        pygame.sprite.Sprite.__init__(self)
        self.collide_type = collide_type
        if collide_type == 'top':
            self.image = pygame.Surface((length, 1))
        if collide_type == 'bottom':
            self.image = pygame.Surface((length, 1))
        if collide_type == 'left':
            self.image = pygame.Surface((1, length))
        if collide_type == 'right':
            self.image = pygame.Surface((1, length))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()

    def update(self):
        pass
