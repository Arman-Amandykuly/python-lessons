import pygame,math
class Graph:
    addx = 20
    addy = 20
    #font = pygame.font.SysFont("comicsansms",10)
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
        for i in range(4*self.inv):
            if(i%8):
                self.rain(i*self.pikuseru/8,self.midy,i*self.pikuseru/8,self.midy-4,width = 2)
                self.rain(-i*self.pikuseru/8,self.midy,-i*self.pikuseru/8,self.midy-4,width = 2)
                self.rain(i*self.pikuseru/8,-self.midy,i*self.pikuseru/8,-self.midy+4,width = 2)
                self.rain(-i*self.pikuseru/8,-self.midy,-i*self.pikuseru/8,-self.midy+4,width = 2)
        for i in range(2*self.inv):
            if(i%4):
                self.rain(i*self.pikuseru/4,self.midy,i*self.pikuseru/4,self.midy-8,width = 2)
                self.rain(-i*self.pikuseru/4,self.midy,-i*self.pikuseru/4,self.midy-8,width = 2)
                self.rain(i*self.pikuseru/4,-self.midy,i*self.pikuseru/4,-self.midy+8,width = 2)
                self.rain(-i*self.pikuseru/4,-self.midy,-i*self.pikuseru/4,-self.midy+8,width = 2)
        for i in range(1,self.inv,2):
            self.rain(i*self.pikuseru/2,self.midy,i*self.pikuseru/2,self.midy-12,width = 2)
            self.rain(-i*self.pikuseru/2,self.midy,-i*self.pikuseru/2,self.midy-12,width = 2)
            self.rain(i*self.pikuseru/2,-self.midy,i*self.pikuseru/2,-self.midy+12,width = 2)
            self.rain(-i*self.pikuseru/2,-self.midy,-i*self.pikuseru/2,-self.midy+12,width = 2)
        for i in range(8*self.inv-8):
            if(i%8):
                self.rain(-self.midx,i*self.pikuseru/16,-self.midx+4,i*self.pikuseru/16,width = 2)
                self.rain(-self.midx,-i*self.pikuseru/16,-self.midx+4,-i*self.pikuseru/16,width = 2)
                self.rain(self.midx,i*self.pikuseru/16,self.midx-4,i*self.pikuseru/16,width = 2)
                self.rain(self.midx,-i*self.pikuseru/16,self.midx-4,-i*self.pikuseru/16,width = 2)
        for i in range(4*self.inv-4):
            if(i%4):
                self.rain(-self.midx,i*self.pikuseru/8,-self.midx+8,i*self.pikuseru/8,width = 2)
                self.rain(-self.midx,-i*self.pikuseru/8,-self.midx+8,-i*self.pikuseru/8,width = 2)
                self.rain(self.midx,i*self.pikuseru/8,self.midx-8,i*self.pikuseru/8,width = 2)
                self.rain(self.midx,-i*self.pikuseru/8,self.midx-8,-i*self.pikuseru/8,width = 2)
        for i in range(1,2*self.inv-4,2):
                self.rain(-self.midx,i*self.pikuseru/4,-self.midx+12,i*self.pikuseru/4,width = 2)
                self.rain(-self.midx,-i*self.pikuseru/4,-self.midx+12,-i*self.pikuseru/4,width = 2)
                self.rain(self.midx,i*self.pikuseru/4,self.midx-12,i*self.pikuseru/4,width = 2)
                self.rain(self.midx,-i*self.pikuseru/4,self.midx-12,-i*self.pikuseru/4,width = 2)
    def graph(self,f,color = (0,0,0)):
        y = f(-1)*self.pikuseru*math.pi
        x = -self.midx
        s = 0
        for i in range(self.w):
            if(x < self.midx and x > -self.midx and y > -self.midy and y<self.midy):
                if(s<20):
                    self.rain(x-1,y,x,f(x/self.pikuseru*math.pi)*self.pikuseru,color,2)
            s += (1+(y-f(x/self.pikuseru*math.pi)*self.pikuseru)**2)**0.5
            y = f(x/self.pikuseru*math.pi)*self.pikuseru
            x+=1
            if(s>33):
                s-=23
        pygame.display.flip()
    def rct(self,x,y):
        self.font = pygame.font.SysFont(None,24)
        self.sin = self.font.render("sin(x)",True,(0,0,0))
        self.cos = self.font.render("cos(x)",True,(0,0,0))
        self.canvas.blit(self.sin,(self.addx+self.pikuseru*2+10,int(self.pikuseru/4)+5))
        self.canvas.blit(self.cos,(self.addx+self.pikuseru*2+10,int(self.pikuseru/4)+25))
        self.rain(self.addx+self.pikuseru*2-10,int(self.pikuseru/4)+8,self.addx+self.pikuseru*2+5,int(self.pikuseru/4)+8,color = (255,0,0))
        self.rain(self.addx+self.pikuseru*2-10,int(self.pikuseru/4)+28,self.addx+self.pikuseru*2-4,int(self.pikuseru/4)+28,color = (0,0,255))
        self.rain(self.addx+self.pikuseru*2-1,int(self.pikuseru/4)+28,self.addx+self.pikuseru*2+5,int(self.pikuseru/4)+28,color = (0,0,255))
        pygame.display.flip()
g = Graph(math.sin,width = 600,height = 450,interval = 4)
g.graph(math.cos,(0,0,255))
done = False
g.rct(2,2)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
pygame.quit()