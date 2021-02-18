import pygame
from pad import Pad


class Player(Pad):
    def __init__(self):
        super(Player, self).__init__()
        self.isDown = False
        self.isUp = False
        self.collide_type = "player"

    def update(self):
        if self.isUp:
            self.rect.y -= self.spd
        elif self.isDown:
            self.rect.y += self.spd
        else:
            pass

    def player_control(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.isUp = True
            if event.key == pygame.K_s:
                self.isDown = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                self.isUp = False
            if event.key == pygame.K_s:
                self.isDown = False