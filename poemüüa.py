import pygame

pygame.init()

# Tekitab 
screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Rainers Game")

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color (e.g., white)
    screen.fill((0, 0, 0))

    pygame.draw.circle(screen, [255, 255, 255], [150, 70], 32)
    pygame.draw.circle(screen, [255, 255, 255], [150, 140], 42)
    pygame.draw.circle(screen, [255, 255, 255], [150, 230], 52)

    pygame.draw.circle(screen, [0, 0, 0], [140, 65], 5)
    pygame.draw.circle(screen, [0, 0, 0], [160, 65], 5)

    pygame.draw.polygon(screen, [255, 0, 0], [[145,75],[155,75],[150,90]] )

    # Update the display
    pygame.display.flip()

# Quit Pygame properly
pygame.quit()
