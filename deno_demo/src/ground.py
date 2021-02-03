import pygame

# ground config
GROUND_HEIGHT = 300
GRAVITY = 2


class Ground(pygame.sprite.Sprite):
    def __init__(self, width):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, 5))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect(y=GROUND_HEIGHT)

        self.ground_height = GROUND_HEIGHT
        self.gravity = GRAVITY
