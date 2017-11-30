#coding:utf-8
#! /usr/bin/env python3

"""Import, get the position, resize and set the transparent background"""

import pygame

from fonction.get_file import get_file_path

def texture_for_sprite(file="", folder="", pos_x=0, pos_y=0, size_x=30, size_y=30, alpha=0):
    """ import a texture, get the sprite position and size in the image,
        convert him to 30*30 pixel if they are not by default
        Attributes: File = name of the picture, must be a PNG (24 bits) format
                    folder = Path folder of the picture
                    pox_x_left_top and pos_y = Indicate the X and Y left top pixel corner
                                        position of the sprite (By default at X:0 and Y:0)
                    size_x and size_y = Size in pixel of the picture (By default 30*30)
                    alpha = Alpha filter image (by default it's no (0)) write : 1 for yes"""

    try:
        # If the picture as no transparent texture
        if alpha == 0:
            texture = pygame.image.load(get_file_path(file, folder)).convert()
            texture.set_clip(pygame.Rect(pos_x, pos_y, size_x, size_y))
            texture_rect = texture.subsurface(texture.get_clip())
            texture_rect = pygame.transform.scale(texture_rect, (30, 30))

        # Need a transparent texture
        else:
            texture = pygame.image.load(get_file_path(file, folder)).convert()
            texture.set_clip(pygame.Rect(pos_x, pos_y, size_x, size_y))
            texture_rect = texture.subsurface(texture.get_clip())
            texture_rect = pygame.transform.scale(texture_rect, (30, 30))
            texture_rect.set_colorkey((0, 0, 0))
        return texture_rect

    except:
        print("Error occured with the texture, need only a picture as PNG format (24 bits)")



def main():
    """Test of transparent background"""
    import fonction.map_generator
    map_lengh = fonction.map_generator.map_size("LevelGame.txt", "map")
    windows_screen = pygame.display.set_mode([int(map_lengh), int(map_lengh)])
    windows_screen.fill((100, 100, 100))

    image = texture_for_sprite("extras-32x-32.png", "picture", 192, 0, 32, 32, 1)
    windows_screen.blit(image, (30, 30))
    pygame.display.flip()

    game_running = 1
    while game_running:
        for event in pygame.event.get():
            # Close game event
            if event.type == QUIT:
                game_running = 0



if __name__ == "__main__":
    main()
