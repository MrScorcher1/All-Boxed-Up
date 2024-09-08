import pygame
import sys
import asyncio

pygame.init()

screen_size = width, height = (800, 600)
display_surface = pygame.display.set_mode(screen_size)

color = {'White': (255, 255, 255),
         'Black:': (0, 0, 0),
         'Red': (255, 0, 0),
         'Green': (0, 150, 0),
         'Blue': (0, 0, 255)
         }
clock = pygame.time.Clock()
counter = 0


async def main():
    while True:
        # force a frame rate of 60 fps
        clock.tick(60)
        # get the mouse position each frame
        mouseX, mouseY = pygame.mouse.get_pos()
        # check the events, and if the QUIT event occurs, close the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # give the option to close the window with ESC
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

        display_surface.fill(color['Green'])  # this is the background
        # draw stuff here. The order determines the layers.

        # flip is all the way at the bottom
        await asyncio.sleep(0)
        pygame.display.flip()

asyncio.run(main())
