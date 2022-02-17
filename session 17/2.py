import pygame
gravity = 0.01
class queen_sprite:
    def  __init__(self,img,target_posn):
        self.image = img
        self.target_posn = target_posn
        self.y_velocity = 0
        self.posn = (target_posn[0],self.y_velocity)
    def  update(self) :
        self.y_velocity = self.y_velocity + gravity
        s
        self.posn = (self.posn[0],self.y_velocity)
        return
    def  draw_queen(self,target_surface):
        target_surface.blit(self.image,(self.target_posn,self.target_posn))
        

pygame.init()
sorlo = pygame.image.load('Idle (10).png')
def  draw_board(boardlist):
    n = len(boardlist)
    color = [(255,0,0),(0,0,0)]
    surfaces = 480
    sq_sz = surfaces // n
    surfaces = sq_sz * n
    c_index=0
    main_surfac = pygame.display.set_mode((surfaces,surfaces))
    for col in range(n):
        c_index = (col+1) % 2 
        for raw in range(n):
            main_surfac.fill(color[c_index % 2],(col * sq_sz,raw * sq_sz,sq_sz,sq_sz))
            c_index = (raw + col) % 2
    for (col,raw) in enumerate(boardlist):
        queen = queen_sprite(sorlo,(col * sq_sz,raw * sq_sz))
        all_sprites.append(queen)
    for sprite in all_sprites :
        sprite.draw_queen(main_surfac)
        sprite.update()
    
    
        
all_sprites=[]
while True:
    ev = pygame.event.poll()
    if ev.type == pygame.QUIT :
        break
     
    draw_board([1,2,4,4,5,6])
    pygame.display.flip()
pygame.quit()
