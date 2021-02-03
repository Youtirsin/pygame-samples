import pygame
from src.player import Player
from src.ground import Ground

pygame.init()

FPS = 120
WINDOW_SIZE = (400, 600)

window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Flappy Demo")
window.fill((255, 255, 255))


def main():
    FPSClock = pygame.time.Clock()

    ground = Ground(WINDOW_SIZE[0])
    player = Player(ground)

    base_group = pygame.sprite.Group()
    base_group.add(ground)
    base_group.add(player)
    base_group.draw(window)

    base_group.update()
    pygame.display.flip()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                player.flappy()

            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                exit()

        # blits
        window.fill((255, 255, 255))

        base_group.draw(window)
        base_group.update()
        pygame.display.update()
        FPSClock.tick(FPS)


if __name__ == "__main__":
    main()
