import pygame

#initialise pygame module
pygame.init()

#game icon
icon = pygame.image.load('spaceinv.png')
pygame.display.set_icon(icon)

#set background
bg = pygame.image.load('spaceinv.png')
picture = pygame.transform.scale(bg, (800, 600))

#spaceship image
space_ship = pygame.image.load("spaceinv.png")

#spaceship coordinates
space_ship_x =400
space_ship_y = 100
space_ship_variable_pos = 0

#space ship function
def display_spaceship(x,y):
    window.blit(space_ship,(x,y))

#set game title
pygame.display.set_caption('space invaders')

#view display
window = pygame.display.set_mode((800,600))

#game loop
running=True
while running:
    window.fill('blue')
   # window.blit(picture,(0,0))
    display_spaceship(space_ship_x,space_ship_y)
    pygame.display.update()
pygame.quit()