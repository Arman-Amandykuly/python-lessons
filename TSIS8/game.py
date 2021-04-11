import pygame,random,os,math
from pygame.locals import *
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()
ww = 700
hh = 400
canvas = pygame.display.set_mode((ww,hh))
pygame.display.set_caption("game")
kek = []
pygame.mixer.music.load("C:\music1.mp3")
class Rect(pygame.Rect):
    def __init__(self,x,y,w,h,color):
        super().__init__(x,y,w,h)
        self.color,self.x,self.y,self.w,self.h = color,x,y,w,h
    def draw(self,surface):
        pygame.draw.rect(surface,self.color,self)
class Line(Rect):
    def __init__(self,road,w,l,color,speed = 6,y0 = 0):
        super().__init__(road.x+road.w/2-w/2,-l+y0,w,l,color)
        self.road = road
        self.sp = speed
        self.w,self.l = w,l
        self.y = -l+y0
        self.color = color
    def update(self):
        self.y+=self.sp
        self.move_ip(0,self.sp)
        if(self.y>=hh):
            self.move_ip(0,-self.y-self.l)
            self.y = -self.l
class Player:
    def __init__(self,w,h,img,road,speed = 5):
        self.sp = speed
        self.x, self.y = 0, road.h-h
        self.w,self.h = w,h
        self.road = road
        self.surf = pygame.Surface((w,h))
        self.rect = self.surf.get_rect(topleft = (road.x,road.h-h))
        self.img = pygame.image.load(os.path.join(os.getcwd(),img)).convert_alpha(canvas)
    def draw(self,surface):
        surface.blit(self.img,self.rect)
    def update(self):
        pk = pygame.key.get_pressed()
        collision = 0
        '''for i in kek:
            if(i.x+i.w>self.x-self.sp+100 and (i.y in range(self.y-10,self.y+self.h-10) or self.y in range(i.y+10,i.y+10+i.h))):
                collision = True'''
        if pk[K_LEFT] and self.x-self.sp>=0 and not collision:
            self.rect.move_ip(-self.sp,0)
            self.x-=self.sp
        collision = 0
        '''for i in kek:
            if(i.x<self.x+self.sp+100 and (i.y in range(self.y-10,self.y+self.h-10) or self.y in range(i.y+10,i.y+10+i.h))):
                collision = True'''
        if pk[K_RIGHT] and self.x+self.sp<=self.road.w-self.w and not collision:
            self.rect.move_ip(self.sp,0)
            self.x+=self.sp
        if pk[K_UP] and self.y-self.sp>=0:
            self.rect.move_ip(0,-self.sp)
            self.y-=self.sp
        if pk[K_DOWN] and self.y+self.sp<=self.road.h-self.h:
            self.rect.move_ip(0,self.sp)
            self.y+=self.sp
road = Rect(100,0,400,hh,(100,100,100))
road.draw(canvas)
pl = Player(50,100,"lol0.png",road)
pl.draw(canvas)
pygame.mixer.music.play()
collided = 0
class Enemy:
    def __init__(self,w,h,img,road,speed = 7,y0 = 0):
        self.w,self.h = w,h
        self.sp = speed
        self.msp = speed
        self.road = road
        self.y = y0
        self.x = random.randint(road.x,road.x+road.w-w)
        self.img = pygame.image.load(os.path.join(os.getcwd(),img))
        self.rect = self.img.get_rect(topleft = (self.x,y0))
    def draw(self,surface):
        surface.blit(self.img,self.rect)
    '''def __del__(self):
        self.rect.__del__()
        del self.surf
        del self.y
        del self.sp
        self.img.__del__()'''
    def update(self):
        self.rect.move_ip(0,self.sp)
        self.y+=self.sp
        if((self.x in range(pl.x+100,pl.x+pl.w+100) and self.y in range(pl.y-10, pl.y+pl.h-10)) or (pl.x in range(self.x-100,self.x+self.w-100) and pl.y in range(self.y+10,self.y+self.h+10)) or (pl.x in range(self.x-100+pl.w,self.x+self.w-100+pl.w) and pl.y in range(self.y+10,self.y+self.h+10))):
            global collided,expx,expy
            expx = (self.x+pl.x-100)/2
            expy = (self.y+pl.y)/2
            collided = 1
            return
        if(self.y>=hh):
            self.x = random.randint(road.x,road.x+road.w-self.w)
            self.rect = self.img.get_rect(topleft = (self.x,-self.h))
            self.y = -self.h
            self.img = pygame.image.load(os.path.join(os.getcwd(),"lol"+str(random.randint(1,4))+".png"))
#class Coin:
#    def __init__
score = 0
class Coin:
    def __init__(self,r,sp = 12,color = (255,255,0)):
        self.r,self.color,self.sp  = r,color,sp
        self.x = random.randint(100,500)
        self.y = -random.randint(r,200)
        self.a = r
        self.al = 0
    def draw(self,surface):
        pygame.draw.ellipse(canvas,self.color,pygame.Rect((int(self.x-self.a),int(self.y-self.r)),(int(2*self.a)+4,int(2*self.r))))
        pygame.draw.rect(canvas,self.color,pygame.Rect(int(self.x-2),int(self.y-self.r),4,2*self.r))
    def update(self):
        self.y+=self.sp
        self.a = abs(math.cos(self.al/20*math.pi*2))*self.r
        self.al = (self.al+1)%20
        b = (self.x in range(pl.x+100,pl.x+pl.w+100) and self.y in range(pl.y,pl.y+pl.h))
        if self.y-self.r>=hh or b:
            self.x = random.randint(100,500)
            self.y = -random.randint(self.r,1000)
            global score
            score+=b
l = [Line(road,20,100,(255,255,255),y0 = i*250) for i in range(2)]
kek = [Enemy(50,100,"lol"+str(random.randint(1,4))+".png",road,y0 = int(-i*(hh+100)//2)) for i in range(2)]
pygame.display.update()
FPS = 60
coin = Coin(20)
coin.draw(canvas)
FramePerSec = pygame.time.Clock()
scl = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
c = [1,1,1]
def gameplay():
    while(True):
        if collided:
            import time
            pygame.mixer.music.stop()
            pygame.mixer.music.load("C:\explosion.wav")
            pygame.mixer.music.play()
            for i in range(1,6):
                img = pygame.image.load(os.path.join(os.getcwd(),"exp"+str(i)+".png"))
                canvas.blit(img,img.get_rect(center = (expx+125,expy+50)))
                pygame.display.update()
                time.sleep(0.2)
            pygame.mixer.music.load("C:\gameover.wav")
            pygame.mixer.music.play()
            for i in range(60):
                font = pygame.font.SysFont("yumincho",i+5)
                g = font.render("GAME OVER",1,(int(255/59*i),255-int(255/59*i),255-int(255/59*i)))
                pygame.display.update()
                canvas.fill((0,120,25))
                road.draw(canvas)
                for i in l:
                    i.draw(canvas)
                coin.draw(canvas)
                pl.draw(canvas)
                for i in kek:
                    i.draw(canvas)
                canvas.blit(g,(140,40))
                time.sleep(0.02)
            time.sleep(1)
            pygame.quit()
            exit()
        pl.update()
        coin.update()
        for i in kek:
            i.update()
        canvas.fill((0,120,25))
        road.draw(canvas)
        for i in l:
            i.update()
            i.draw(canvas)
        coin.draw(canvas)
        pl.draw(canvas)
        for i in kek:
            i.draw(canvas)
        font = pygame.font.SysFont("arial",40)
        if(scl[0]<=0):
            c[0] = 1
        if(scl[1]<=0):
            c[1] = 1
        if(scl[2]<=0):
            c[2] = 1
        if(scl[0]>=255):
            c[0] = -1
        if(scl[1]>=255):
            c[1] = -1
        if(scl[2]>=255):
            c[2] = -1
        fr = font.render("Score: "+str(score),1,tuple(scl))
        scl[0]+=c[0]
        scl[1]+=c[1]
        scl[2]+=c[2]
        canvas.blit(fr,(520,100))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        FramePerSec.tick(FPS)
#def menu():
gameplay()
pygame.quit()
exit()
s = input()
pygame.quit()