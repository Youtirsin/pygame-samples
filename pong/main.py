import pygame
from player import Player
from ball import Ball
from border import Border

pygame.init()

FPS = 60
WINSIZE = (600, 400)

window = pygame.display.set_mode(WINSIZE)
pygame.display.set_caption("Pong Demo")

player = Player()
player.rect.center = (15, 160)
ball = Ball()
ball.rect.x = 0
ball.rect.y = 0

border_top = Border('top',WINSIZE[0])
border_bottom = Border('bottom',WINSIZE[0])
border_left = Border('left',WINSIZE[1])
border_right = Border('right',WINSIZE[1])

border_top.rect.bottom = 0
border_bottom.rect.top = WINSIZE[1]
border_left.rect.right = 0
border_right.rect.left = WINSIZE[0]

border_grp = pygame.sprite.Group()
ball_grp = pygame.sprite.Group()
player_grp = pygame.sprite.Group()

border_grp.add(border_top)
border_grp.add(border_bottom)
border_grp.add(border_left)
border_grp.add(border_right)
player_grp.add(player)
ball_grp.add(ball)


FPSClock = pygame.time.Clock()


def main():
    border_grp.draw(window)
    ball_grp.draw(window)
    pygame.display.flip()
    while 1:
        for event in pygame.event.get():
            player.player_control(event)
            if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
                pygame.quit()
                exit(0)

        ball.collide(border_grp)
        ball.collide(player_grp)

        window.fill((0, 0, 0))

        ball_grp.update()
        player_grp.update()

        border_grp.draw(window)
        ball_grp.draw(window)
        player_grp.draw(window)

        pygame.display.update()
        FPSClock.tick(FPS)


if __name__ == '__main__':
    main()
