import pygame
from src.player import Player
from src.ground import Ground
from src.obstacle import Obstacle

pygame.init()

FPS = 60
WINDOW_SIZE = (600, 400)

window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Deno Demo")
window.fill((255, 255, 255))

# -------- config --------
GRAVITY = 1


def main():
    FPSClock = pygame.time.Clock()

    ground = Ground(WINDOW_SIZE[0])
    player = Player(ground)
    ob = Obstacle(30)

    base_group = pygame.sprite.Group()
    base_group.add(ground)
    base_group.add(player)
    base_group.add(ob)
    base_group.draw(window)

    base_group.update()
    pygame.display.flip()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                player.jump()

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
