import pygame
pygame.init()
hh,ww = 500,500
m = 100
canvas = pygame.display.set_mode((ww,hh))
def c(c,r):
    xy = pygame.mouse.get_pos()
    pygame.draw.circle(canvas,c,xy,r)
def r(c,h,w):
    x,y = pygame.mouse.get_pos()
    pygame.draw.rect(canvas,c,pygame.Rect(int(x-w/2),int(y-h/2),w,h))
class Button(pygame.sprite.Sprite):
    def __init__(self,color,w,h,text,f):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([w,h])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.txt = text
        self.font = pygame.font.SysFont(f,h-10)
    def draw(self):
        canvas.blit(self.image,self.rect)
        canvas.blit(self.font.render(self.txt,1,(255,255,255)),(self.rect.x+5,self.rect.y+5))
button = Button((255,0,0),50,20,"Red","kalam")
button.draw()
while 1:
    if pygame.mouse.get_pressed()[0]:
        c((255,255,255),20)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()