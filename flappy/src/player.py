import pygame

# player config
JUMP_HEIGHT = 80


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40, 40))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect(center = (50, 150))

        self.flappyCap = 0
        self.falling = True

    def update(self):
        # update movement
        if self.flappyCap <= 0:
            if self.falling:
                self.rect.bottom += 4
        # flappy
        else:
            self.rect.bottom -= 8
            self.flappyCap -= 8

    def flappy(self):
        self.flappyCap += JUMP_HEIGHT
