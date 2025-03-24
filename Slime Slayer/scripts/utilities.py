import pygame as pg


def load_image(path): 
    base_image_path = '\\Users\\Ralph\\OneDrive\\Ralph VS Code folder\\Slime Slayer\\data\\'
    # if your image a transparent background use convert_alpha() instead of convert()
    img  = pg.image.load(base_image_path + path).convert_alpha()
    # makes any color that it (0,0,0) transparent
    #img.set_colorkey((0,0,0))
    return img
    

