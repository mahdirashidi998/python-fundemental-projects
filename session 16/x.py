import pygame
pygame.init()
while True:
    ev = pygame.event.poll()
    if ev.type == pygame.QUIT:
        break
    wn = pygame.display.set_mode((1000,1000))
    wn.fill((200,100,50))
    wn.fill((100,200,50),(100,100,100,100))
    sepehr = pygame.image.load('StackableTreeHouse-parts')
    wn.blit(sepehr,(500,500))
    pygame.display.flip()
pygame.quit()