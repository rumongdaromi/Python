from locale import D_FMT
import pygame
import random
import 보스몬스터
import 보스방전용케릭
import 패배시작
import 승리시작

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 900 # 가로 크기
screen_height = 900 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))
# 화면 타이틀(제목) 설정
pygame.display.set_caption("과제 제출용 게임") #게임 이름
# FPS 초당 프레임 변수 설정
clock = pygame.time.Clock()
position = (300,500)
# 배경 이미지 불러오기
background = pygame.image.load("/Users/imin-ug/Python/게임프로그래밍/파이게임/겜프프로젝트/진짜제출폴더임/은신처.png")
background_left = pygame.transform.flip(background, True, False)

# 이동할 좌표
scroll = 10
# 객체의 처음 위치
position_a = 10
position_b= 800
# 적1의 처음 위치
position_a1 = 800
position_b1= 700

size_a = 800
size_b = 600
n =0
right_TF = False
left_TF = False
D_TF = False
k_up_DF = False
background_x1 = 0
background_xy = background.get_rect().size
background_x = background_xy[0]

#플레이어 체력 바 
helthly_bar = 140

boss_hp1 = 850
boss_hp2 = 850
#데미지 타임
helthly_count = 0
# 이동 속도
character_speed = 0.5

# 캐릭터 생성
player = 보스방전용케릭.AnimatedSprite(position=(position_a, position_b)) # 플레이어 위치 지정
#적 생성

boss = 보스몬스터.AnimatedSprite(position=(500,200))
boss.state =0
boss_x_pos = 500
boss_y_pos = 200
boss_size = boss.images[boss.index].get_rect().size  # 이미지 크기를 구해옴
boss_width = boss_size[0] # 적의 가로크기
boss_height = boss_size[1] # 적의 세로크기

boss_hp_bar = 500
boss_hp_bar2 = 500
player_size = player.images[player.index].get_rect().size
player_width = player_size[0] # 캐릭터의 가로 크기
player_height = player_size[1] # 캐릭터의 세로 크기
player_x_position = position_a #이부분과 위의 플레이어 위치 지정 시 좌표가 맞아야 가능   
player_y_position = position_b

all_sprites = pygame.sprite.Group(player)
enemy_sprites =pygame.sprite.Group(boss)

attact_sound = pygame.mixer.Sound( "/Users/imin-ug/Python/게임프로그래밍/파이게임/겜프프로젝트/진짜제출폴더임/음악파일/공격모션소리2.wav" )
hit_sound = pygame.mixer.Sound( "/Users/imin-ug/Python/게임프로그래밍/파이게임/겜프프로젝트/진짜제출폴더임/음악파일/데미지.wav" )

bomb_image =  pygame.image.load('/Users/imin-ug/Python/게임프로그래밍/파이게임/겜프프로젝트/fire2.png')
bombs = []
def runGame():
    global bomb_image,bombs
    bomb_image = pygame.image.load('/Users/imin-ug/Python/게임프로그래밍/파이게임/겜프프로젝트/fire2.png')
    bomb_image = pygame.transform.scale(bomb_image, (40, 40))

runGame()
fire = 5
fire_count  = 0
        
# 이동할 좌표# 화면 세로 크기 중간지점에 적 캐릭터의 세로 위치
def main():
    global background_x,background_x1,background_left,background_왼쪽,right_TF,left_TF,D_TF
    global position_a1,position_b1,k_up_DF,boss_x_pos,boss_y_pos,boss_hp_bar,boss_hp_bar2
    global helthly_bar,helthly_count,boss_hp1,boss_hp2,bomb_image,bombs,fire,fire_count
    boss.state = 0
    hp_count = 0
    
    for i in range(fire):
                rect = pygame.Rect(bomb_image.get_rect())
                rect.left = random.randint(0, 900)
                rect.top = -100
                dy = random.randint(12, 18) ## 떨어지는 속도
                bombs.append({'rect': rect, 'dy': dy})
            
    pygame.mixer.music.load( "/Users/imin-ug/Python/게임프로그래밍/파이게임/겜프프로젝트/진짜제출폴더임/음악파일/보스방.mp3" )
    pygame.mixer.music.play(-1)

    running = True # 게임이 진행중인지 확인하기
    while running:
        if not bombs or fire_count == 1:
            for i in range(fire):
                rect = pygame.Rect(bomb_image.get_rect())
                rect.left = random.randint(0, 900)
                rect.top = -100
                dy = random.randint(12, 18) ## 떨어지는 속도
                bombs.append({'rect': rect, 'dy': dy})
        runGame()
        
        fire_count = 0
        
        player.animation_time = round(100 / len(player.images * 100), 2)
        #print(player_size)
        #print(player.rect.x,player.rect.y)
        mt = clock.tick(60) / 1000
        dt = clock.tick(80) # 게임화면의 초당 프레임 수 설정
        
        #print("fps : " + str(clock.get_fps())) #프레임 수 확인
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_SPACE]):
                if player.isJump == 2:
                    player.jump(1)
                    
        for event in pygame.event.get(): # running 중 키보드나,마우스 입력값(이벤트)을 체크해주는것
            if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는지
                running = False # 게임이 진행중이 아님

            if event.type == pygame.KEYDOWN: #키가 눌러졌는지 확인
                
                if event.key == pygame.K_d:
                    player.state = 2
                    D_TF = True
                elif event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로
                    player.direction = "left"
                    player.state = 1  #이부분이군요 ㅠㅠ    
                    left_TF = True
                        
                elif event.key == pygame.K_RIGHT: # 캐릭터를 오른쪽으로
                    player.direction = "right"
                    player.state = 1
                    #position_a1 -= 10
                    right_TF = True
                #elif event.key -- pygame.K_DOWN: # 캐릭터를 아래로
                elif event.key == pygame.K_SPACE:
                        if player.isJump == 0:
                            player.jump(1)
                        elif player.isJump == 1:
                            player.jump(2)
                
                elif event.key == pygame.K_UP:
                        k_up_DF = True
                #공격 d키 눌리면 공격모션을 함            
        
            if event.type == pygame.KEYUP: # 방향키를 떼면 멈춤
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    player.velocity_x = 0
                    player.state = 0
                    right_TF = False
                    left_TF = False
                    D_TF = False

        boss_rect = boss.images[boss.index].get_rect()
        boss_rect.left = boss_x_pos
        boss_rect.top = boss_y_pos
        
        for bomb in bombs:
            if bomb['rect'].colliderect(player):
                done = True
            screen.blit(bomb_image, bomb['rect'])
                        
        b2 = background_x * 2
        
        if right_TF == True:
            #배경 오른쪽 끝이  800보다 작아진다면 다시 돌려라  배경 오른쪽 끝 좌표가 <= screen_width
            if b2 <= background_x:
                pass
            else:             
                position_a1 -= 10 
        
        elif D_TF == True:
            attact_sound.play()
            print(player.index)

        elif left_TF == True:
            if background_x1>= 0:
                background_x1 = 0
            else:
                boss_x_pos += 10
                       
        # X 경계값 설정
        if player.rect.x < 0:
            player.rect.x = 0
        elif player.rect.x > screen_width - player_width:
            player.rect.x = screen_width - player_width
        # Y 경계값 설정
        if player.rect.y < 0:
            player.rect.y = 0
        elif player.rect.y > screen_height - player_height:
                player.rect.y = screen_height - player_height   
                
        
        for bomb in bombs:
            bomb['rect'].top += bomb['dy']
            if bomb['rect'].top > 900:
                bombs.remove(bomb)
                rect = pygame.Rect(bomb_image.get_rect())
                rect.left = random.randint(0,800)
                rect.top = -100
                dy = random.randint(3, 9)
                bombs.append({'rect': rect, 'dy': dy})
        
        # 충돌 처리를 위한 rect 정보 업데이트 (실제 좌표를 알아야 충돌처리가 됨)
            if player.rect.colliderect(boss_rect):               
                helthly_count+=1
                if player.state ==2:
                    helthly_count += 1
                    if helthly_count >30:
                        if hp_count == 0:
                            boss_hp2 -= 10
                        elif hp_count == 1:
                            boss_hp1 -= 10                          
                        helthly_count = 0
                print("cndehd")
                
            if helthly_bar <= 70: 
                    helthly_bar = 70
                    패배시작.mainmenu()
                    pygame.quit()   
            elif boss_hp1 < 200:   
                    승리시작.mainmenu()
                    pygame.quit()                
            if boss_hp2 < 200:
                hp_count = 1     
                boss_hp2 = 200
                fire = 15
                boss.state = 1
                fire_count = 1
            
                    
            if boss_hp1 < 200:
                boss_hp1 = 200
                
                
                

        
        background_왼쪽 = background_x1
            
 
            
        if  k_up_DF == True:        
            pass
            
                    
        #  running = False # 종료 코드
        screen.blit(background, (background_x1,-50)) # 배경 그리기(background 가 표시되는 위치)
        screen.blit(background_left, (background_x,-50))
        
        enemy_sprites.update(mt)
        enemy_sprites.draw(screen)
        
        all_sprites.update(mt)
        all_sprites.draw(screen)
        
        #player hp바 
        pygame.draw.line(screen, ('gray'), (player.rect.x+70, player.rect.y-50), (player.rect.x+140, player.rect.y-50),10)
        pygame.draw.line(screen, ('red'), (player.rect.x+70, player.rect.y-50), (player.rect.x+helthly_bar, player.rect.y-50),10)
        
        
        pygame.draw.line(screen, ('gray'), (200, boss.rect.y-150), (850, boss.rect.y-150),15)
        pygame.draw.line(screen, ('gray'), (200, boss.rect.y-130), (850, boss.rect.y-130),15)
        
        pygame.draw.line(screen, ('red'), (200, boss.rect.y-150), (boss_hp1, boss.rect.y-150),15)
        pygame.draw.line(screen, ('red'), (200, boss.rect.y-130), (boss_hp2, boss.rect.y-130),15)
        
        for bomb in bombs:
            if bomb['rect'].colliderect(player.rect):
                done = True
                helthly_bar -= 10
                hit_sound.play()
                bombs.remove(bomb)
                if helthly_bar == 0:
                        game_over = True
            screen.blit(bomb_image, bomb['rect'])
        pygame.display.update() # 게임화면을 지속적으로 그리기(for 문도는동안 계속)
    # pygame 종료
    pygame.quit()
    
if __name__ == '__main__':
    main()