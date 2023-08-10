from locale import D_FMT
import pygame
import char_image
import 발록
import 아이스골램
import 좀비
import potal
import random as r
import 제출용2
import 보스방




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
background = pygame.image.load("/Users/imin-ug/Python/게임프로그래밍/파이게임/겜프프로젝트/bg2/w6.png")
background_left = pygame.transform.flip(background, True, False)

mySound = pygame.mixer.Sound( "/Users/imin-ug/Python/게임프로그래밍/파이게임/겜프프로젝트/진짜제출폴더임/음악파일/던전브금.wav" )
attact_sound = pygame.mixer.Sound( "/Users/imin-ug/Python/게임프로그래밍/파이게임/겜프프로젝트/진짜제출폴더임/음악파일/공격모션소리2.wav" )
hit_sound = pygame.mixer.Sound( "/Users/imin-ug/Python/게임프로그래밍/파이게임/겜프프로젝트/진짜제출폴더임/음악파일/데미지.wav" )

enemy_num = 9
enemy_hp = []
for i in range(0,enemy_num):
    enemy_hp.append(140)
# 이동할 좌표
scroll = 10
# 객체의 처음 위치
position_a = 10
position_b= 800
# 적1의 처음 위치
position_a1 = 800
position_b1= 700

# 아이스골램의 위치
position_a2 = 1100
position_b2= 700


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
#데미지 타임
helthly_count = 0

emeny_helthy_bar = 140

ice_golem_bar = 140
zombi_helthy_bar = 160

# 이동 속도
character_speed = 0.5
position = ()

# 캐릭터 생성
position_a12 = 800
position_b12= 700
player = char_image.AnimatedSprite(position=(position_a, position_b)) # 플레이어 위치 지정

abc = []

for i in range(0,enemy_num):
    abc.append(아이스골램.AnimatedSprite(position=(position_a12, position_b12)))
    position_a12+= 300
    enemy_copy = pygame.sprite.Group(abc[i])
    

#적 생성
emeny1 = 아이스골램.AnimatedSprite(position=(position_a1,position_b1))
ice_golem = 아이스골램.AnimatedSprite(position=(position_a2,position_b2))

#포탈을 불러옴
potal = potal.AnimatedSprite(position=(3800,600))
all_sprites = pygame.sprite.Group(potal,player)
enemy_sprites =pygame.sprite.Group(emeny1,ice_golem,abc)

player_size = player.images[player.index].get_rect().size
player_width = player_size[0] # 캐릭터의 가로 크기
player_height = player_size[1] # 캐릭터의 세로 크기
player_x_position = position_a #이부분과 위의 플레이어 위치 지정 시 좌표가 맞아야 가능   
player_y_position = position_b


enemy1_size = emeny1.images[emeny1.index].get_rect().size
enemy1_width = enemy1_size[0] # 캐릭터의 가로 크기
enemy1_height = enemy1_size[1] # 캐릭터의 세로 크기
enemy1_x_position = position_a1
enemy1_y_position = position_b1


move_count = 0
move_icegolem = 0
     
def ice_golem_move():
    ice_golem.state = 0
    global move_icegolem
    move_icegolem += 1
    print(move_icegolem)
    if move_icegolem <= 20 and move_icegolem  >= 0:
        ice_golem.state = 1
        ice_golem.direction = 'left'
        ice_golem.rect.x -= 5
    elif move_icegolem > 20 and move_icegolem <= 30:
        print("idle")
        ice_golem.state = 0
    elif move_icegolem > 30 and move_icegolem <= 50:
        print("right")
        ice_golem.direction = 'right'
        ice_golem.rect.x += 5
        ice_golem.state = 1
              
    elif move_icegolem > 50:
        move_icegolem = 0
        
def  enemy_move():
    emeny1.state = 0
    global move_count
    move_count += 1
    print(move_count)
    
    if move_count <= 50 and move_count  >= 0:
        emeny1.state = 1
        emeny1.direction = 'left'
        emeny1.rect.x -= 1
        for i in range(0,enemy_num ):
            abc[i].direction = 'left'
            abc[i].state = 1
    elif move_count > 50 and move_count <= 100:
        print("idle")
        emeny1.state = 0
        for i in range(0,enemy_num ):
            abc[i].state = 0
    elif move_count > 100 and move_count <= 150:
        print("right")
        emeny1.direction = 'right'
        emeny1.rect.x += 1
        emeny1.state = 1
        for i in range(0,enemy_num ):
            abc[i].direction = 'right'
            abc[i].state = 1
    elif move_count > 150 and move_count <= 200:
        print("idle")
        emeny1.state = 0
        for i in range(0,enemy_num ):
            abc[i].state = 0
    elif move_count > 200 and move_count <= 250:
        print("right")
        emeny1.state = 2
        for i in range(0,enemy_num ):
            abc[i].state = 2
    
    elif move_count > 250 and move_count <= 300:
        print("left")
        emeny1.direction = 'left'
        emeny1.state = 2
        for i in range(0,enemy_num ):
            abc[i].direction = 'left'
            abc[i].state = 2
        
    elif move_count > 300:
        move_count = 0

# 이동할 좌표# 화면 세로 크기 중간지점에 적 캐릭터의 세로 위치
def main():
    map_count = 3+enemy_num
    global background_x,background_x1,background_left,background_왼쪽,right_TF,left_TF,D_TF
    global enemy1_x_position,enemy1_y_position,position_a1,position_b1,position_a2,position_b2,k_up_DF
    global helthly_bar,helthly_count,emeny_helthy_bar,ice_golem_bar
    pygame.mixer.music.load( "/Users/imin-ug/Python/게임프로그래밍/파이게임/겜프프로젝트/진짜제출폴더임/음악파일/배경3.mp3" )
    pygame.mixer.music.play(-1)
    running = True # 게임이 진행중인지 확인하기
    while running:

        if player.state == 2:
            attact_sound.play()
        
        print("배경크기" ,background_x)
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
                
        
            if event.type == pygame.KEYUP: # 키가 안눌려있으면 멈추게 하는 코드
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    player.velocity_x = 0
                    player.state = 0
                    right_TF = False
                    left_TF = False
                    D_TF = False

            
        b2 = background_x * 2
        print("b2 = >" ,b2)
        
        if right_TF == True:
            #배경 오른쪽 끝이  800보다 작아진다면 다시 돌려라  배경 오른쪽 끝 좌표가 <= screen_width
            if b2 <= background_x:
                print("끝")
                pass
            else:
                background_x1 -= scroll
                background_x -= scroll
                for i in range(0,enemy_num):
                    abc[i].rect.x -= 10
                emeny1.rect.x -= 10
                ice_golem.rect.x -= 10
                potal.rect.x -= 10
                position_a1 -= 10 
        
        elif D_TF == True:
            print(player.index)

        elif left_TF == True:
            if background_x1>= 0:
                background_x1 = 0
            else:
                background_x1 += scroll
                background_x += scroll
                emeny1.rect.x += 10
                ice_golem.rect.x += 10
                for i in range(0,enemy_num):
                    abc[i].rect.x += 10

                potal.rect.x += 10
                position_a1 += 10
            # enemy1_x_position += scroll
        
            
        
        enemy_move()
        ice_golem_move()
        
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
                
        # x 경계값 설정
        if ice_golem.rect.x < 0:
            ice_golem.rect.x = 0
        elif ice_golem.rect.x > screen_width - player_width:
            ice_golem.rect.x = screen_width - player_width 
                
                

        # 충돌 처리를 위한 rect 정보 업데이트 (실제 좌표를 알아야 충돌처리가 됨)

        
        background_왼쪽 = background_x1
            
    # 피통
        if helthly_bar <= 70: 
            helthly_bar = 70
        if emeny_helthy_bar <=70:  
            emeny_helthy_bar = 70
            
        if player.rect.colliderect(ice_golem.rect):
            helthly_count+=1
            if helthly_count >30 and player.state != 2 :
                helthly_bar -= 10
                hit_sound.play()
                helthly_count = 0
            if player.state ==2:
                helthly_count += 1
                if helthly_count >30:
                    if player.direction == 'right':
                        ice_golem.rect.x += 20
                    elif player.direction == 'left':
                        ice_golem.rect.x -= 20
                    ice_golem_bar-= 10
                    helthly_count = 0
                    
        for i in range(0,enemy_num):
                    if abc[i].rect.colliderect(player):
                        print('zzzzzzz')
                        helthly_count+=1
                        if helthly_count >30 and emeny1.state == 2 :
                            helthly_bar -= 10
                            hit_sound.play()
                            if player.direction == 'right':
                                    player.rect.x -= 80
                            elif player.direction == 'left':
                                    player.rect.x += 80
                            helthly_count = 0
                        if player.state ==2:
                            helthly_count += 1
                            if helthly_count >30:
                                if player.direction == 'right':
                                    abc[i].rect.x += 50
                                elif player.direction == 'left':
                                    abc[i].rect.x -= 50
                                enemy_hp[i] -= 10
                                if enemy_hp[i] <= 0:
                                    enemy_copy.remove(abc[i])
                                helthly_count = 0
         
        if player.rect.colliderect(emeny1.rect):
            print("충돌임 ㄹㅇ")
            helthly_count+=1
            if helthly_count >30 and emeny1.state == 2 :
                helthly_bar -= 10
                hit_sound.play()
                if player.direction == 'right':
                        player.rect.x -= 80
                elif player.direction == 'left':
                        player.rect.x += 80
                helthly_count = 0
            if player.state ==2:
                helthly_count += 1
                if helthly_count >30:
                    if player.direction == 'right':
                        emeny1.rect.x += 50
                    elif player.direction == 'left':
                        emeny1.rect.x -= 50
                    emeny_helthy_bar-= 10
                    helthly_count = 0
                    
            if helthly_count > 30 and player.state == 2:
                zombi_helthy_bar -= 10
                helthly_count = 0
                
        if  k_up_DF == True:        
            if player.rect.colliderect(potal.rect): 
                #if map_count <= 5:   
                    print("포탈임 ㄹㅇ")
                    보스방.main()
                    pygame.quit()

            
                    
        #  running = False # 종료 코드
        screen.blit(background, (background_x1,0)) # 배경 그리기(background 가 표시되는 위치)
        screen.blit(background_left, (background_x,0))

        bc =100
        enemy_copy.update(mt)
        enemy_copy.draw(screen)
        enemy_sprites.update(mt)
        enemy_sprites.draw(screen)
        all_sprites.update(mt)
        all_sprites.draw(screen)

        #player hp바 
        pygame.draw.line(screen, ('gray'), (player.rect.x+70, player.rect.y-50), (player.rect.x+140, player.rect.y-50),10)
        pygame.draw.line(screen, ('red'), (player.rect.x+70, player.rect.y-50), (player.rect.x+helthly_bar, player.rect.y-50),10)
        
        if emeny_helthy_bar> 70:
            pygame.draw.line(screen, ('gray'), (emeny1.rect.x+70, emeny1.rect.y-50), (emeny1.rect.x+140, emeny1.rect.y-50),10)
            pygame.draw.line(screen, ('red'), (emeny1.rect.x+70, emeny1.rect.y-50), (emeny1.rect.x+emeny_helthy_bar, emeny1.rect.y-50),10)
        else:
            emeny1.rect.x = 0
            emeny1.rect.y = 0
            enemy_sprites.remove(emeny1)
            map_count -= 1 

        for i in range(0,enemy_num):
            if enemy_hp[i] > 70:
                pygame.draw.line(screen, ('gray'), (abc[i].rect.x+70, abc[i].rect.y-50), (abc[i].rect.x+140, abc[i].rect.y-50),10)
                pygame.draw.line(screen, ('red'), (abc[i].rect.x+70, abc[i].rect.y-50), (abc[i].rect.x+enemy_hp[i], abc[i].rect.y-50),10)
        
        for i in range(0, enemy_num):                       
            if enemy_hp[i] <= 70:
                abc[i].rect.x = -1200
                enemy_copy.remove(abc[i])
                map_count -= 1 
                
        
        
        if ice_golem_bar > 70:
            pygame.draw.line(screen, ('gray'), (ice_golem.rect.x+70, ice_golem.rect.y-50), (ice_golem.rect.x+140, ice_golem.rect.y-50),10)
            pygame.draw.line(screen, ('red'), (ice_golem.rect.x+70, ice_golem.rect.y-50), (ice_golem.rect.x+ice_golem_bar, ice_golem.rect.y-50),10)
        else:# hp가 없으면 좌표를 0,0으로 보내고 골램을 스프라이트에서 제거
            ice_golem.rect.x = 0 
            ice_golem.rect.y = 0
            enemy_sprites.remove(ice_golem)
            map_count -= 1 
   
                
              
        
        if emeny_helthy_bar> 70:
            pygame.draw.line(screen, ('gray'), (emeny1.rect.x+70, emeny1.rect.y-50), (emeny1.rect.x+140, emeny1.rect.y-50),10)
            pygame.draw.line(screen, ('red'), (emeny1.rect.x+70, emeny1.rect.y-50), (emeny1.rect.x+emeny_helthy_bar, emeny1.rect.y-50),10)
        else:
            emeny1.rect.x = 0
            emeny1.rect.y = 0
            enemy_sprites.remove(emeny1)
            map_count -= 1 
            
        pygame.display.update() # 게임화면을 지속적으로 그리기(for 문도는동안 계속)

    # pygame 종료
    pygame.quit()
    
if __name__ == '__main__':
    main()