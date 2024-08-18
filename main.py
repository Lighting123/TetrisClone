import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((300, 500))
clock = pygame.time.Clock()
running = True
pygame.display.set_caption('Tetris Clone')

# blocks
block_1 = pygame.image.load('assets/sprite_0.png')


while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # draw the game
    screen.blit(pygame.transform.scale_by(block_1, 3), (0,0))

    # update the screen
    pygame.display.flip()

    # limit the frame rate to 60 fps
    clock.tick(60)

pygame.quit()