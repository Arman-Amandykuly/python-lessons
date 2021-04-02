import pygame,math
class Graph:
    addx = 20
    addy = 20
    def rain(self,x1,y1,x2,y2,color = (0,0,0),width = 1):
        int(x1+self.addx+self.midx)
        pygame.draw.line(self.canvas,color,(int(x1+self.addx+self.midx),int(self.midy-y1+self.addy)),(int(x2+self.addx+self.midx),int(-y2+self.addy+self.midy)),width)
    def __init__(self,f = lambda x:x,width=400,height=300,interval=5,istr = False):
        pygame.init()
        self.func,self.w,self.h,self.iv = f,width,height,interval
        self.canvas = pygame.display.set_mode((self.w+2*self.addx,self.h+2*self.addy))
        self.canvas.fill((255,255,255))
        self.inv = interval
        self.pikuseru = width/self.inv
        self.midx = self.w/2
        self.midy = self.h/2
        for i in range(int(self.inv/2)+1):
            self.rain(i*self.pikuseru,-self.midy,i*self.pikuseru,self.midy,(150,150,150))
            self.rain(-i*self.pikuseru,-self.midy,-i*self.pikuseru,self.midy,(150,150,150))
        for i in range(int(2*self.w//(self.pikuseru))):
            self.rain(-self.midx,i*self.pikuseru/4,self.midx,i*self.pikuseru/4,(150,150,150))
            self.rain(-self.midx,-i*self.pikuseru/4,self.midx,-i*self.pikuseru/4,(150,150,150))
        self.rain(0,-self.midy,0,self.midy)
        self.rain(-self.midx,0,self.midx,0)
        y = self.func(-1*math.pi)*self.pikuseru
        x = -self.midx
        for i in range(self.w):
            if(x < self.midx and x > -self.midx and y > -self.midy and y<self.midy):
                self.rain(x-1,y,x,self.func(x/self.pikuseru*math.pi)*self.pikuseru,(255,0,0),2)
            y = self.func(x/self.pikuseru*math.pi)*self.pikuseru
            x+=1
        pygame.draw.rect(self.canvas,(0,0,0),pygame.Rect((self.addx,self.addy),(self.w,self.h)),3)
        pygame.display.flip()
    def graph(self,f,color = (0,0,0)):
        y = f(-1)*self.pikuseru*math.pi
        x = -self.midx
        for i in range(self.w):
            if(x < self.midx and x > -self.midx and y > -self.midy and y<self.midy):
                self.rain(x-1,y,x,f(x/self.pikuseru*math.pi)*self.pikuseru,color,2)
            y = f(x/self.pikuseru*math.pi)*self.pikuseru
            x+=1
        pygame.display.flip()
g = Graph(math.sin,interval = 3)
g.graph(math.cos,(0,0,255))