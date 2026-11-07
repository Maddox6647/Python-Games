"""
Example of loading a background image that is not as wide as the screen, and
tiling it to fill the screen.

"""
import pygame

# Initialize Pygame
pygame.init()

from pathlib import Path
assets = Path(__file__).parent / 'images'

# Set up display
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Tiled Background')
def make_tiled_bg(screen):
    # Create a list of six different colors
    colors = [
        (255, 0, 0),(0, 255, 0),(0, 0, 255),(255, 255, 0),(255, 0, 255),(0, 255, 255)]
    tiles = []
    for color in colors:
            tile = pygame.Surface((100, screen.get_height()))
            tile.fill(color)
            tiles.append(tile)
    image = pygame.Surface((screen.get_width(), screen.get_height()))

    # Tile the background image in the x-direction
    for x in range(0, screen.get_width(), 100):
        tile_number = x//100
        image.blit(tiles[tile_number], (x, 0))
        
    return image

background = make_tiled_bg(screen)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background,(0,0))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()



