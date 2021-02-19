import pygame
from random import randint

# config
BALL_INIT_SPD = 1
BALL_INIT_DIRECTION = 60


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40, 40))
        pygame.draw.circle(self.image, (255, 255, 255), (20, 20), 20)
        self.rect = self.image.get_rect()
        self.spd = BALL_INIT_SPD
        self.move_val = [2, 3]
        self.isAlive = True

    def update(self):
        if self.isAlive:
            self.rect.x += self.spd * self.move_val[0]
            self.rect.y += self.spd * self.move_val[1]

    def collide(self, grp):
        if pygame.sprite.spritecollideany(self, grp):
            target = pygame.sprite.spritecollideany(self, grp)
            if target.collide_type == 'top':
                self.move_val[1] = randint(1, 5)
                self.move_val[0] = self.move_val[0] / abs(self.move_val[0]) * randint(1, 5)
            if target.collide_type == 'bottom':
                self.move_val[1] = 0 - randint(1, 5)
                self.move_val[0] = self.move_val[0] / abs(self.move_val[0]) * randint(1, 5)
            # game over
            if target.collide_type == 'left':
                # self.move_val[0] = randint(1, 5)
                # self.move_val[1] = self.move_val[1] / abs(self.move_val[1]) * randint(1, 5)
                print("GAME OVER")
                pygame.draw.circle(self.image, (255, 0, 0), (20, 20), 20)
                self.isAlive = False

            if target.collide_type == 'right':
                self.move_val[0] = 0 - randint(1, 5)
                self.move_val[1] = self.move_val[1] / abs(self.move_val[1]) * randint(1, 5)

            if target.collide_type == 'player':
                self.move_val[0] = randint(1, 5)
                self.move_val[1] = self.move_val[1] / abs(self.move_val[1]) * randint(1, 5)
            if target.collide_type == 'bot':
                self.move_val[0] = 0 - randint(1, 5)
                self.move_val[1] = self.move_val[1] / abs(self.move_val[1]) * randint(1, 5)