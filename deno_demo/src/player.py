import pygame
from src.obstacle import Obstacle
# player config
PLAYER_COLOR = (0, 0, 0)
INIT_POS = (50, 200)
JUMP_HEIGHT = 70
JUMP_SPEED = 5


class Player(pygame.sprite.Sprite):
    def __init__(self, ground):
        super(Player, self).__init__()
        self.image = pygame.Surface((60, 60))
        self.image.fill(PLAYER_COLOR)
        self.rect = self.image.get_rect(x = INIT_POS[0], y = INIT_POS[1])

        self.ground = ground
        self.falling = False
        self.jumping = False

    def update(self):
        # update movement
        # fall by gravity
        if not self.jumping and self.rect.bottom <= self.ground.ground_height:
            self.rect.bottom += self.ground.gravity
        # jump
        if self.jumping and self.rect.bottom > self.ground.ground_height - JUMP_HEIGHT:
            self.rect.bottom -= JUMP_SPEED
        # fall after jump
        if self.rect.bottom <= self.ground.ground_height - JUMP_HEIGHT:
            self.jumping = False

    def jump(self):
        # jump
        self.jumping = True

    def hit(self, grp):
        target = pygame.sprite.spritecollideany(self, grp)
        print(type(target) == Obstacle)
