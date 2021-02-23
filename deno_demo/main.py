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

ground = Ground(WINDOW_SIZE[0])
player = Player(ground)
ob = Obstacle(30)

grp = pygame.sprite.Group()
ob_grp = pygame.sprite.Group()

grp.add(ground)
grp.add(player)
ob_grp.add(ob)
grp.draw(window)


def main():
    FPSClock = pygame.time.Clock()

    grp.update()
    ob_grp.update()
    pygame.display.flip()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                player.jump()

            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                exit()
        # player collide detection
        player.hit(ob_grp)

        # draw
        window.fill((255, 255, 255))

        grp.draw(window)
        ob_grp.draw(window)
        grp.update()
        ob_grp.update()
        pygame.display.update()
        FPSClock.tick(FPS)


if __name__ == "__main__":
    main()
