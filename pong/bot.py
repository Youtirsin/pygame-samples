import pygame
from pad import Pad


# invincible bot :D
class Bot(Pad):
    def __init__(self, ball):
        super(Bot, self).__init__()
        self.collide_type = "bot"
        self.followTo = ball

    def update(self):
        self.rect.centery = self.followTo.rect.centery
