import pygame  #Impordime pygamei

pygame.init()  #Käivitame pygamei

#Loome akna suurusega 300x300 pikslit
screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Lumememm - Rainer Hints")  #Määrame aknale pealkirja

#alustame tsükklit
running = True
while running:
    #Kontrollime sündmusi staatust
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Kui vajutatakse akna risti, lõpetame tsükli

    #Täidame ekraani taustavärviga (must)
    screen.fill((0, 0, 0))

    #Joonistame kolm valget ringi
    pygame.draw.circle(screen, [255, 255, 255], [150, 70], 32)
    pygame.draw.circle(screen, [255, 255, 255], [150, 140], 42)
    pygame.draw.circle(screen, [255, 255, 255], [150, 230], 52)

    #Joonistame kaks musta ringi silmadeks
    pygame.draw.circle(screen, [0, 0, 0], [140, 65], 5)
    pygame.draw.circle(screen, [0, 0, 0], [160, 65], 5)

    #Joonistame punase kolmnurga lumememme ninaks
    pygame.draw.polygon(screen, [255, 0, 0], [[145, 75], [155, 75], [150, 90]])

    #Uuendame ekraani
    pygame.display.flip()

#Sulgeme pygamei kui aken sulgub
pygame.quit()
