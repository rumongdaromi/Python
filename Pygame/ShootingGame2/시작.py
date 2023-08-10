from turtle import back
import pygame
import random
import os
import sys
import time

# ----- 게임창 위치설정 -----

win_posx = 700
win_posy = 300
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (win_posx, win_posy)

# ----- 전역 -----

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700
FPS = 60
background = pygame.image.load("/Users/imin-ug/Python/병주겜프/U2.png")
boom = pygame.image.load("/Users/imin-ug/Python/병주겜프/boom.png")
boom = pygame.transform.scale(boom, (100, 100))
background = pygame.transform.scale(background, (900, 700))
background1 = background.copy()

c1 = pygame.image.load("/Users/imin-ug/Python/병주겜프/우주선.png")
c1 = pygame.transform.scale(c1, (100, 100))
c2 = pygame.image.load("/Users/imin-ug/Python/병주겜프/우주선2.png")
c2 = pygame.transform.scale(c2, (100, 100))
c3 = pygame.image.load("/Users/imin-ug/Python/병주겜프/우주선3.png")
c3 = pygame.transform.scale(c3, (100, 100))

c1_rect = c1.get_rect()
c2_rect = c2.get_rect()
c3_rect = c3.get_rect()
c1_rect.x = 100
c1_rect.y = 400
c2_rect.x = 400
c2_rect.y = 400
c3_rect.x = 700
c3_rect.y = 400

score = 0
player_c = 0
playtime = 1

Change_image = 0

def drawOb(obj,x,y): #폭발 효과 주는 함수 
    global screen
    screen.blit(boom,(x,y))
    
def initialize_game(width, height):
    pygame.init()
    surface = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Pygame Shmup")
    return surface

def game_loop(surface):
    clock = pygame.time.Clock()
    sprite_group = pygame.sprite.Group()
    mobs = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    player = PlayerShip()
    global player_health
    player_health= 100
    global score,Change_image,player_c
    score = 0
    sprite_group.add(player)
    for i in range(2):
        enemy = Mob()
        sprite_group.add(enemy)
        mobs.add(enemy)
    
    background_y = 0
    background_y2 = SCREEN_HEIGHT  
    
    running = True
    choice = True
        
    start = 0   
    sound = pygame.mixer.Sound("/Users/imin-ug/Python/병주겜프/배경음악.mp3")
    sound.play(-1)
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False
                if event.key == pygame.K_SPACE:
                    player.shoot(sprite_group, bullets)
           
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start == 0:
                    for i in (c1_rect,c2_rect,c3_rect):
                            if i.collidepoint(event.pos):
                                start = 1
                                if i == c1_rect:
                                    player.image = pygame.image.load("/Users/imin-ug/Python/병주겜프/우주선.png")
                                elif i == c2_rect:
                                    player.image = pygame.image.load("/Users/imin-ug/Python/병주겜프/우주선2.png")
                                elif i == c3_rect:
                                    player.image = pygame.image.load("/Users/imin-ug/Python/병주겜프/우주선3.png")
                                sound.stop()
                                sound = pygame.mixer.Sound("/Users/imin-ug/Python/병주겜프/메인배경음악.mp3")
                                sound.play(-1)
        if start == 0:
            screen.blit(background,(0,0))            
            screen.blit(c1,(100,400))
            screen.blit(c2,(400,400))
            screen.blit(c3,(700,400)) 
            font = pygame.font.SysFont('malgungothic',100)
            image = font.render(f' Pygame project ', True, 'yellow')
            surface.blit(image,(170,100))
                
            
        
                   
        if start ==1:
            sprite_group.update()
            hits = pygame.sprite.spritecollide(player, mobs, True)
            if hits:
                print('a mob hits player!')
                mob = Mob()
                sprite_group.add(mobs)
                mobs.add(mob)
                player_health -= 1
                Change_image += 1
                print(Change_image)
                if Change_image ==7:
                    Change_image = 0
                
                if player_health < 0:
                    gameover(surface)
                    close_game()
                    restart()
                    
            background_y += 2
            background_y2 += 2
            
            if background_y >= SCREEN_HEIGHT:
                background_y = -SCREEN_HEIGHT
            
            if background_y2 >=  SCREEN_HEIGHT:
                background_y2 = -SCREEN_HEIGHT
                
                
            screen.blit(background, (0,background_y))
            screen.blit(background1, (0,background_y2))
            
            hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
            for hit in hits:
                hit_mob = pygame.mixer.Sound("/Users/imin-ug/Python/병주겜프/폭탄효과음.wav")
                hit_mob.play()
                boom_c = 0
                while boom_c < 5:
                    drawOb(boom,hit.rect.x,hit.rect.y)
                    boom_c+=1
                print(Change_image)
                if Change_image == 7:
                    Change_image = 0
                mob = Mob()
                sprite_group.add(mobs)
                mobs.add(mob)
                Change_image += 1
                score += 10
            sprite_group.draw(surface)
            score_update(surface)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
    print('game played: ',playtime)

def score_update(surface):
    font = pygame.font.SysFont('malgungothic',35)
    image = font.render(f'  SCORE : {score}  HP: {player_health} ', True, 'yellow')
    pos = image.get_rect()
    pos.move_ip(20,20)
    surface.blit(image, pos)

def gameover(surface):
    font = pygame.font.SysFont('malgungothic',50)
    image = font.render('GAME OVER', True, 'yellow')
    pos = image.get_rect()
    pos.move_ip(50, int(SCREEN_HEIGHT/2))
    surface.blit(image, pos)
    pygame.display.update()
    time.sleep(2)

def close_game():
    pygame.quit()
    print('Game closed')

def restart():
    screen = initialize_game(SCREEN_WIDTH,SCREEN_HEIGHT)
    game_loop(screen)
    close_game()

class PlayerShip(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        a = pygame.image.load("/Users/imin-ug/Python/병주겜프/우주선.png")
        self.image = pygame.transform.scale(a, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.centerx = int(SCREEN_WIDTH / 2)
        self.rect.centery = SCREEN_HEIGHT - 20
        self.speedx = 0
        self.speedy = 0

    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            self.speedx = -10
        if keystate[pygame.K_d]:
            self.speedx = 10
        if keystate[pygame.K_w]:
            self.speedy = -10
        if keystate[pygame.K_s]:
            self.speedy = 10
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0

    def shoot(self, all_sprites,bullets):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)


class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        global Change_image
        meteor = pygame.image.load("/Users/imin-ug/Python/병주겜프/운석.png")
        self.image = pygame.transform.scale(meteor, (40, 40))
        if Change_image == 2:
            meteor = pygame.image.load("/Users/imin-ug/Python/병주겜프/운석2.png")
            self.image = pygame.transform.scale(meteor, (60, 60))
        if Change_image == 4:
            meteor = pygame.image.load("/Users/imin-ug/Python/병주겜프/운석3.png")
            self.image = pygame.transform.scale(meteor, (100, 100))
        elif Change_image == 6: 
            meteor = pygame.image.load("/Users/imin-ug/Python/병주겜프/운석4.png")
            self.image = pygame.transform.scale(meteor, (400, 400))
        
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)
        self.direction_change = False

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.top > SCREEN_HEIGHT + 10 or self.rect.left < -25 or self.rect.right > SCREEN_WIDTH + 20:
            self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(3, 8)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, player_x, player_y):
        pygame.sprite.Sprite.__init__(self)
        boom_s = pygame.mixer.Sound("/Users/imin-ug/Python/병주겜프/총소리.mp3")
        boom_s.play()
        msl = pygame.image.load("/Users/imin-ug/Python/병주겜프/미사일1.png")
        self.image = pygame.transform.scale(msl, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.bottom = player_y
        self.rect.centerx = player_x
        self.speedy = - 10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()

if __name__ == '__main__':
    screen = initialize_game(SCREEN_WIDTH,SCREEN_HEIGHT)
    game_loop(screen)
    sys.exit()
