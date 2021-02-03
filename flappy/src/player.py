import pygame

# player config
PLAYER_COLOR = (0, 0, 0)
INIT_POS = (50, 150)
JUMP_HEIGHT = 72
JUMP_SPEED = 4


class Player(pygame.sprite.Sprite):
    def __init__(self, ground):
        pygame.sprite.Sprite.__init__(self)
        # super().__init__(self)
        self.image = pygame.Surface((40, 40))
        self.image.fill(PLAYER_COLOR)
        self.rect = self.image.get_rect(x = INIT_POS[0], y = INIT_POS[1])

        self.ground = ground
        self.flappyCap = 0

    def update(self):
        # update movement
        # fall by gravity
        if self.flappyCap == 0 and self.rect.bottom <= self.ground.ground_height:
            self.rect.bottom += self.ground.gravity
        # flappy
        if self.flappyCap != 0:
            self.rect.bottom -= JUMP_SPEED
            self.flappyCap -= JUMP_SPEED

    def flappy(self):
        self.flappyCap += JUMP_HEIGHT
