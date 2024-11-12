import pygame
import random


def main():
    try:
        pygame.init()



        # You can draw the mole with this snippet:
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()


        mole_image = pygame.image.load("mole.png")




        x, y = 0,0








        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mole_moved = mole_image.get_rect(topleft=(x*32,y *32))

                    if mole_moved.collidepoint(event.pos):
                        x, y = random.randint(0,19),random.randint(0,15)





            screen.fill("light green")

            screen.blit(mole_image, mole_image.get_rect(topleft=(x * 32, y * 32)))

            color = (0,0,0)
            for i in range(21):
             pygame.draw.line(screen, color, (i*32, 0), (i*32, 512))

            for j in range(16):
                pygame.draw.line(screen, color, ( 0, j*32), (640, j *32))

            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()