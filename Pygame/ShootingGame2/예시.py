from itertools import count
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

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
FPS = 60
count = 501
score = 0
playtime = 1
item_count = 0
item_using = 0
num = 3
zamin = []

# ----- 색상 -----

BLACK = 0, 0, 0
WHITE = 255,255,255
RED = 255, 0, 0
GREEN1 = 25, 102, 25
GREEN2 = 51, 204, 51
GREEN3 = 233, 249, 185
BLUE = 17, 17, 212
BLUE2 = 0, 0, 255
YELLOW = 255, 255, 0
LIGHT_PINK1 = 255, 230, 255
LIGHT_PINK2 = 255, 204, 255
background = pygame.image.load("C:/Users/rladu/OneDrive/바탕 화면/김연규/우주.png")
background = pygame.transform.scale(background, (700, 500))

def initialize_game(width, height):
    pygame.init()
    surface = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Pygame Shmup")
    return surface



def game_loop(surface):
    clock = pygame.time.Clock()
    sprite_group = pygame.sprite.Group()
    mobs = pygame.sprite.Group()
    items = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    bolet = pygame.sprite.Group()
    b_coli = pygame.sprite.Group()
    player = PlayerShip()
    booser = ZaminKoo() 
    
    global player_health
    player_health= 100
    global boss_health
    boss_health = 1000
    global score, count, item_count, num,zamin
    score = 0
    enemy_count = 0
    boss_count = 0
    global zamin_count
    zamin_count = 0
    shot = 0
    c = 1
    sprite_group.add(player)
    sprite_group.add(booser)
    for i in range(num):
        enemy = Mob()
        sprite_group.add(enemy)
        mobs.add(enemy)     
    running = True 
    while running:
        if boss_health <= 0 or player_health <= 0:
               running = False
        if count <=500:
            count += 1
        shot += 1 
        
        if score == 100 and zamin_count == 0:
            booser.rect.y = 0 # 화면 밖에 있던 보스의 좌표를 0으로 만들어서 화면 안으로 이동  
            
        if booser.rect.y >= 0:
            if shot % 40 == 0 and shot != 0:
                booser.shoot1(sprite_group, bolet)
                
            if score == 0 and boss_count == 0:
                    sprite_group.add(booser)
                    b_coli.add(booser)
                    boss_count = 1
            booser.update() 
            
        for i in bullets:
            if i.rect.colliderect(booser.rect):
                    boss_health -= 10
                    i.kill()
        
        for i in bolet:
            if i.rect.colliderect(player.rect):
                    player_health -= 10
                    i.kill()
            
            
        if score % 100 == 0 and item_count == 0 and score != 0:
            for i in range(1):
                item1  = item()
                sprite_group.add(item1)
                items.add(item1) 
            item_count = 1  
        
        if score % 100 != 0:
             enemy_count = 0
             
        if score % 200 == 0 and enemy_count == 0 and score != 0 :
                for i in range(c):
                    enemy = Mob()
                    sprite_group.add(enemy)
                    mobs.add(enemy)
                enemy_count = 1 
                c += 1
                
        
        
        if boss_health <= 750:
            booser.image= zamin[1]
        if boss_health <= 500:
            booser.image= zamin[2]
        if boss_health <= 250:
            booser.image= zamin[3]
              
        
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False
                if event.key == pygame.K_SPACE:
                    player.shoot(sprite_group, bullets)
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                player.shoot(sprite_group, bullets)
                booser.shoot(sprite_group, bolet)
                
        sprite_group.update()

        hits = pygame.sprite.groupcollide(mobs, bullets, True,True)
        for hit in hits:
            mob = Mob()
            sprite_group.add(mobs)
            mobs.add(mob)
            score += 10
        
        hits1 = pygame.sprite.groupcollide(items, bullets, True,True)
        for hit in hits1:
            mob = Mob()
            item1 = item()
            hit.kill()
            item_count = 0
            
        
        for i in mobs:
            if i.rect.collidepoint(player.rect.center):
                    player_health -= 1
                    i.rect.x = -100
                    i.rect.y = -100
                    i.kill()
                    enemy = Mob()
                    sprite_group.add(enemy)
                    mobs.add(enemy)
                     
        for i in items:
             if i.rect.collidepoint(player.rect.center):
                     player_health -= 1
                     i.rect.x = -100
                     i.rect.y = -100
                     i.kill()
                     item_count = 0
                     count = 0
                     

        screen.blit(background, (0,0))
        sprite_group.draw(surface)
        score_update(surface)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
    print('game played: ',playtime) 

def score_update(surface):
    font = pygame.font.SysFont('malgungothic',35)
    image = font.render(f'  score : {score}  HP: {player_health} ', True, 'YELLOW')
    image2 = font.render(f'  HP: {boss_health} ', True, 'YELLOW')
    pos = image.get_rect()
    pos1 = image2.get_rect()
    pos.move_ip(20,20)
    pos1.move_ip(20,20)
    pygame.draw.rect(image, BLACK,(pos.x-20, pos.y-20, pos.width, pos.height), 2)
    pygame.draw.rect(image2, BLACK,(pos.x-20, pos.y-20, pos.width, pos.height), 2)
    surface.blit(image, pos)
    surface.blit(image2, (500,10))

def gameover(surface):
    font = pygame.font.SysFont('malgungothic',50)
    image = font.render('GAME OVER', True, BLACK)
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
        a = pygame.image.load("C:/Users/rladu/OneDrive/바탕 화면/김연규/ship.png")
        self.image = pygame.transform.scale(a, (50, 80))
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
        global count
        bullet = Bullet(self.rect.centerx, self.rect.top)  
        if count <500: ###################################################################
            bullet2 = item_Bullet(self.rect.centerx+10, self.rect.top)
            bullet = Bullet(self.rect.centerx-10, self.rect.top)
            all_sprites.add(bullet2)
            bullets.add(bullet2)
        all_sprites.add(bullet)
        bullets.add(bullet)
        


class ZaminKoo(pygame.sprite.Sprite):
    def __init__(self):
        global zamin
        self.rect = pygame.Rect((350,-300), (120,120))
        pygame.sprite.Sprite.__init__(self)
        zamin.append(pygame.image.load("C:/Users/rladu/OneDrive/바탕 화면/김연규/제목.png"))
        zamin.append(pygame.image.load("C:/Users/rladu/OneDrive/바탕 화면/김연규/제목 2.png"))
        zamin.append(pygame.image.load("C:/Users/rladu/OneDrive/바탕 화면/김연규/제목 3.png"))
        zamin.append(pygame.image.load("C:/Users/rladu/OneDrive/바탕 화면/김연규/제목 4.png"))
        self.images = [pygame.transform.scale(image, (120,120)) for image in zamin]
  
        self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        self.speedx = random.randrange(-3, 3)
        self.direction_change = False
        
        self.index = 0
        self.image = zamin[self.index]

    def update(self):
        self.rect.x += self.speedx
        if self.rect.left < -25:
            self.speedx = random.randrange(1, 3)
            self.rect.x += 10  #뺀만큼에서부터 다시 시작
        if self.rect.right > SCREEN_WIDTH + 20:
            self.rect.x -= 10
            self.speedx = random.randrange(-3, 1)
            
    def shoot1(self, all_sprites,bolet):
        global count,boss_health
        Bobullet1 = Boss_Bullet(self.rect.centerx, self.rect.top)  
        if  boss_health <500: ###################################################################
             print(self.rect.centerx)
             Boss_Bullet1 = Boss_Bullet(self.rect.centerx+50, self.rect.top)
             Boss_Bullet2 = Boss_Bullet(self.rect.centerx-50, self.rect.top)
             all_sprites.add(Boss_Bullet2,Boss_Bullet2)
             bolet.add(Boss_Bullet2,Boss_Bullet2)
        else:    
            all_sprites.add(Bobullet1)
            bolet.add(Bobullet1)

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        a = pygame.image.load("C:/Users/rladu/OneDrive/바탕 화면/김연규/운석.png")
        self.image = pygame.transform.scale(a, (30, 40))
        self.color = random.choice([BLACK, BLUE, RED, GREEN1, YELLOW])
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 5)
        self.speedx = random.randrange(-3, 3)
        self.direction_change = False

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.top > SCREEN_HEIGHT + 10 or self.rect.left < -25 or self.rect.right > SCREEN_WIDTH + 20:
            self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(3, 8)
            
class item(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        a = pygame.image.load("C:/Users/rladu/OneDrive/바탕 화면/김연규/루난.jpg")
        self.image = pygame.transform.scale(a, (30, 40))
        self.color = random.choice([BLACK, BLUE, RED, GREEN1, YELLOW])
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 5)
        self.speedx = random.randrange(-3, 3)
        self.direction_change = False
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > SCREEN_HEIGHT + 10 or self.rect.left < -25 or self.rect.right > SCREEN_WIDTH + 20:
            self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(3, 8)
            
class hil_item(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        a = pygame.image.load("C:/Users/rladu/OneDrive/바탕 화면/김연규/루난.jpg")
        self.image = pygame.transform.scale(a, (30, 40))
        self.color = random.choice([BLACK, BLUE, RED, GREEN1, YELLOW])
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 5)
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
        self.image = pygame.Surface((10,20))
        self.image.fill(GREEN1)
        self.rect = self.image.get_rect()
        self.rect.bottom = player_y
        self.rect.centerx = player_x
        self.speedy = - 10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()
            
class item_Bullet(pygame.sprite.Sprite):
    def __init__(self, player_x, player_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10,20))
        self.image.fill(GREEN1)
        self.rect = self.image.get_rect()
        self.rect.bottom = player_y
        self.rect.centerx = player_x
        self.speedy = - 10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()
            
class Boss_Bullet(pygame.sprite.Sprite):
    def __init__(self, boss_x, boss_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10,20))
        self.image.fill(GREEN1)
        self.rect = self.image.get_rect()
        self.rect.bottom = boss_y+150
        self.rect.centerx = boss_x
        self.speedy = + 10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom  > 600:
            self.kill()

if __name__ == '__main__':
    screen = initialize_game(SCREEN_WIDTH,SCREEN_HEIGHT)
    game_loop(screen)
    sys.exit()