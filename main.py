import pygame,sys
pygame.init()
screen_width = 900
screen_height = 600
screen= pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
            screen.fill('black')
    pygame.display.update()
    clock.tick(60)