import sys
import pygame
import C_go
import 진짜제출폴더임.Game_image

from pygame.locals import QUIT, Rect, KEYDOWN, K_SPACE
w = 650
h = 700
pygame.init()
pygame.key.set_repeat(5, 5)
SURFACE = pygame.display.set_mode((w,h))
FPSCLOCK = pygame.time.Clock()

def main():
    """ 메인 루틴 """
    
    B1_x = 0
    B1_y = 0
    B2_x = 1800
    count = 0
    space_count = 0
    user_x = 200
    user_y = 600
    user_G = 0
    score = 0
    sysfont = pygame.font.SysFont(None, 36)
    user= []
    user.append(pygame.image.load("/Users/imin-ug/Python/게임프로그래밍/파이게임/겜프프로젝트/게임리소스/c1.png"))
    user.append(pygame.image.load("/Users/imin-ug/Python/게임프로그래밍/파이게임/겜프프로젝트/게임리소스/c2.png"))
    bang_image = pygame.image.load("/Users/imin-ug/Python/게임프로그래밍/파이게임/겜프프로젝트/게임리소스/c2.png")

    s_X = user_x
    s_y = user_y

    game_over = False

    while True:
            
        move_instance = C_go.Cvar(user_x)
        image_resorce = Game_image.images()
        
        space_count = 1
        is_space_down = False
        is_right_arrow = False
        is_left_arrow = False
        is_D_down = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    is_space_down = True
                elif event.key == pygame.K_DOWN:
                    is_down_arrow = True
                elif event.key == pygame.K_UP:
                    is_up_arrow = True
                elif event.key == pygame.K_LEFT:
                    is_left_arrow = True
                elif event.key == pygame.K_RIGHT:
                    is_right_arrow = True

        # 내 캐릭터를 이동
        if not game_over:
            score += 10
            if is_right_arrow:
                user_x = move_instance.move()
                user[count]
                count = (count+1) % 2
                if B1_x >= -500:                
                    B1_x -= 30
                    if user_x >=500:
                        user_x = 100
                        B2_x = 0                
            elif is_left_arrow:
                user_x += -6
                user[count]
                count = (count+1) % 2
                if B1_x <= -100: 
                    B1_x += 30
                    
            elif is_space_down:
                s_X = user_x+10
                space_count = 0
                print("눌림")
        SURFACE.fill((0, 0, 0))
        SURFACE.blit(image_resorce.image_save('login'), (B1_x,B1_y))
        SURFACE.blit(user[count], (user_x, user_y))
        score_image = sysfont.render("score is {}".format(score),
                                     True, (0, 0, 225))
        SURFACE.blit(score_image, (600, 20))
        
        s_X = user_x
        
        while space_count == 0:
            s_X += 20
            SURFACE.blit(image_resorce.image_save('swoosh'), (s_X+10, s_y))
            if s_X > user_x + 200:
                s_X == user_x
                break
            
        if game_over:
            SURFACE.blit(bang_image, (0, 0))

        pygame.display.update()
        FPSCLOCK.tick(30)

if __name__ == '__main__':
    main()
