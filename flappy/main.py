import pygame
from src.player import Player
from src.ground import Ground

pygame.init()

FPS = 60
WINDOW_SIZE = (400, 600)

window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Flappy Demo")
window.fill((255, 255, 255))


def main():
    FPSClock = pygame.time.Clock()

    ground = Ground()
    player = Player()

    group = pygame.sprite.Group()

    group.add(ground)
    group.add(player)

    group.draw(window)

    group.update()
    pygame.display.flip()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                player.flappy()

            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                exit()

        # blits
        window.fill((255, 255, 255))

        group.draw(window)

        # gravity work
        falled = pygame.sprite.spritecollide(ground, group, False)
        if falled.count(player):
            player.falling = False
        else:
            player.falling = True

        group.update()
        pygame.display.update()
        FPSClock.tick(FPS)


if __name__ == "__main__":
    main()
