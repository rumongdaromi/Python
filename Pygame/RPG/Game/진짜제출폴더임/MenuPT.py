import pygame
import time
import sys
import 연습용
num12 = 0

a = pygame.image.load("/Users/imin-ug/Python/게임프로그래밍/파이게임/겜프프로젝트/w4.jpg")
startImg = pygame.image.load("/Users/imin-ug/Python/게임프로그래밍/파이게임/겜프프로젝트/starticon.png")
quitImg = pygame.image.load("/Users/imin-ug/Python/게임프로그래밍/파이게임/겜프프로젝트/quiticon.png")
clickStartImg = pygame.image.load("/Users/imin-ug/Python/게임프로그래밍/파이게임/겜프프로젝트/clickedStartIcon.png")
clickQuitImg = pygame.image.load("/Users/imin-ug/Python/게임프로그래밍/파이게임/겜프프로젝트/clickedQuitIcon.png")
char = pygame.image.load('/Users/imin-ug/Python/게임프로그래밍/파이게임/겜프프로젝트/진짜제출폴더임/유저 케릭터 파일/outImgs-4/0.png')
black =pygame.image.load('/Users/imin-ug/Python/게임프로그래밍/파이게임/겜프프로젝트/진짜제출폴더임/보스몹/idle/0.png')

gameDisplay = pygame.display.set_mode((900,900))
pygame.display.set_caption("M_RPG")
clock = pygame.time.Clock()

class Button:
    def __init__(self, img_in, x, y, width, height, img_act, x_act, y_act, action = None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            gameDisplay.blit(img_act,(x_act, y_act))
            if click[0] and action != None:
                time.sleep(1)
                action()
        else:
            gameDisplay.blit(img_in,(x,y))

def quitgame():
    pygame.quit()
    sys.exit()

def startgame():
    연습용.main()
    pygame.quit()

def mainmenu():
    pygame.init()
    menu = True

    while menu:
        menu = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.blit(a,(0,0))
        gameDisplay.blit(char,(100,300))
        gameDisplay.blit(black,(600,200))
        #titletext = gameDisplay.blit(titleImg, (350,350))
        startButton = Button(startImg,400,450,180,20,clickStartImg,400,450,startgame) #500,400 x,y좌표 180,20은 감지되는 박스의 범위
        quitButton = Button(quitImg,400,520,60,20,clickQuitImg,400,520,quitgame)
        pygame.display.update()
        clock.tick(15)
                
mainmenu()
game_loop()

