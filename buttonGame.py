import asyncio
import sys
from Button import *

pygame.init()

screen_size = width, height = (800, 600)
display_surface = pygame.display.set_mode(screen_size)

color = {'Red': (255, 0, 0),
         'Orange': (255, 120, 0),
         'Yellow': (255, 255, 0),
         'Green': (0, 180, 0),
         'Blue': (0, 0, 255),
         'Indigo': (75, 0, 130),
         'Pink': (255, 23, 197),
         'Purple': (238, 130, 238),
         'Grey': (128, 128, 128),
         'Light_Grey': (220, 220, 220),
         'Dark_Grey': (70, 70, 70),
         'Brown': (125, 70, 20),
         'White': (255, 255, 255),
         'Black': (0, 0, 0)
         }
clock = pygame.time.Clock()


async def main():
    counter = 0
    testButton = Button(width // 2 - 175, height // 2 - 50, 350, 100, None, "Test")
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

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if testButton.hovered(mouseX, mouseY):
                    counter += 1
                    testButton.text = str(counter)

        display_surface.fill(color['Green'])  # this is the background
        # draw stuff here. The order determines the layers.
        testButton.show(display_surface, color['Green'], pygame.font.SysFont("comicsansms", 50, True), color['Black'])

        # flip is all the way at the bottom
        await asyncio.sleep(0)
        pygame.display.flip()

asyncio.run(main())
