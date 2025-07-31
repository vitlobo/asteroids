import pygame
from constants import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    should_exit = False
    while should_exit == False:
          for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
          screen.fill((0,0,0))
          pygame.display.flip()

def fill(self, color):
    pygame.Surface.fill(color)


if __name__ == "__main__":
    main()