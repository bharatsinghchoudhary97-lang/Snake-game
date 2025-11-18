import pygame, random, sys
pygame.init()
W,H=600,600; G=20; GW=W//G; GH=H//G
s=pygame.display.set_mode((W,H)); pygame.display.set_caption('Snake')
c=pygame.time.Clock(); f=pygame.font.SysFont('arial',35); sf=pygame.font.SysFont('arial',25)
def grid():
 for x in range(0,W,G):pygame.draw.line(s,(40,40,40),(x,0),(x,H))
 for y in range(0,H,G):pygame.draw.line(s,(40,40,40),(0,y),(W,y))
def loop():
 snake=[(GW//2,GH//2)]; d=(1,0); score=0; speed=10
 food=(random.randint(0,GW-1),random.randint(0,GH-1))
 while True:
  for e in pygame.event.get():
   if e.type==pygame.QUIT:pygame.quit();sys.exit()
   if e.type==pygame.KEYDOWN:
    if e.key==pygame.K_UP and d!=(0,1):d=(0,-1)
    if e.key==pygame.K_DOWN and d!=(0,-1):d=(0,1)
    if e.key==pygame.K_LEFT and d!=(1,0):d=(-1,0)
    if e.key==pygame.K_RIGHT and d!=(-1,0):d=(1,0)
  h=(snake[0][0]+d[0],snake[0][1]+d[1])
  if h[0]<0 or h[0]>=GW or h[1]<0 or h[1]>=GH or h in snake:over(score)
  snake.insert(0,h)
  if h==food:score+=1;food=(random.randint(0,GW-1),random.randint(0,GH-1));speed=min(25,speed+0.5)
  else:snake.pop()
  s.fill((0,0,0));grid()
  for i,p in enumerate(snake):
   pygame.draw.rect(s,(0,155,0)if i==0 else(0,255,0),(p[0]*G,p[1]*G,G,G))
   pygame.draw.rect(s,(255,255,255),(p[0]*G,p[1]*G,G,G),1)
  pygame.draw.rect(s,(255,0,0),(food[0]*G,food[1]*G,G,G))
  s.blit(sf.render(f"Score: {score}",1,(255,255,255)),(10,10))
  pygame.display.update();c.tick(speed)
def over(score):
 s.fill((0,0,0))
 s.blit(f.render("GAME OVER",1,(255,0,0)),(W//2-120,200))
 s.blit(f.render(f"Score: {score}",1,(255,255,255)),(W//2-100,280))
 s.blit(sf.render("R=Restart Q=Quit",1,(255,255,255)),(W//2-130,360))
 pygame.display.update()
 while True:
  for e in pygame.event.get():
   if e.type==pygame.QUIT:pygame.quit();sys.exit()
   if e.type==pygame.KEYDOWN:
    if e.key==pygame.K_r:loop()
    if e.key==pygame.K_q:pygame.quit();sys.exit()
loop()
