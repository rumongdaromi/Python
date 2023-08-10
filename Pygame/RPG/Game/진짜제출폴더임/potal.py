import pygame
import sys

# 스크린 전체 크기 지정
SCREEN_WIDTH = 1020
SCREEN_HEIGHT = 700
 
# pygame 초기화
pygame.init()
 
# 스크린 객체 저장
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("pygame Sprite")
 
# FPS를 위한 Clock 생성
clock = pygame.time.Clock()
FPS = 60

# 속도와 질량 기본 값
VELOCITY = 7
MASS = 2
 
BACKGROUND_COLOR = pygame.Color('white')
 
class AnimatedSprite(pygame.sprite.Sprite):
 
    def __init__(self, position):
        super(AnimatedSprite, self).__init__()
        
        self.image = ""
        self.dx = 0
        self.dy = 0
        self.rect = ""
        self.isJump = 0
        self.v = VELOCITY # 속도
        self.m = MASS  # 질량
 
        # 이미지를 Rect안에 넣기 위해 Rect의 크기 지정
        # 이미지의 크기와 같게 하거나, 크기를 다르게 한다면 pygame.transform.scale을 사용하여 rect 안에
        # 이미지를 맞추도록 한다.
        size = (181, 170)

        # 여러장의 이미지를 리스트로 저장한다. 이미지 경로는 자신들의 경로를 사용한다.
        images = []
        
        # 서있는 상태 0 ~ 5
        images.append(pygame.image.load('/Users/imin-ug/Python/게임프로그래밍/파이게임/겜프프로젝트/진짜제출폴더임/0.png'))
        images.append(pygame.image.load('/Users/imin-ug/Python/게임프로그래밍/파이게임/겜프프로젝트/진짜제출폴더임/1.png'))
        images.append(pygame.image.load('/Users/imin-ug/Python/게임프로그래밍/파이게임/겜프프로젝트/진짜제출폴더임/2.png'))
        images.append(pygame.image.load('/Users/imin-ug/Python/게임프로그래밍/파이게임/겜프프로젝트/진짜제출폴더임/3.png'))
                                    
 

       #rect 만들기
        self.rect = pygame.Rect(position, size)

        # Rect 크기와 Image 크기 맞추기. pygame.transform.scale
        self.images = [pygame.transform.scale(image, size) for image in images]
 
        # 원본 캐릭터 이미지들
        self.images_right = images
        # 캐릭터 이미지가 오른쪽을 보고 있는데, 왼쪽으로 보도록 하기 위해서는
        # 이미지를 세로 기준으로 좌우로 뒤집이 준다. pygame.transform.flip 메서드 사용
        self.images_left = [pygame.transform.flip(image, True, False) for image in images]
       
        # 캐릭터의 현재 상태
        # 0 - idle 상태, 1 - 걷고 있는 상태
        self.state = 0
        # 방향
        self.direction = 'right'
        # 속도
        self.velocity_x = 0
 
        # 캐릭터의 첫번째 이미지
        self.index = 0
        self.image = images[self.index]
 
        # 1초에 보여줄 1장의 이미지 시간을 계산, 소수점 3자리까지 반올림
        self.animation_time = round(100 / len(self.images * 100), 2)

        # mt와 결합하여 animation_time을 계산할 시간 초기화
        self.current_time = 0
        
    def jump(self, j):
        self.isJump = j
    
    def move_x(self):
        self.rect.x += self.dx
 
 
    def update(self, mt):
       
        if self.state == 0:
            count = 6 #플레이어 이미지의 갯수와 동일해야함
            start_Index = 0
            self.velocity_x = 0
        elif self.state == 1:
            count = 8
            start_Index = 6
            self.velocity_x = 4
        
        elif self.state == 2:
            count = 12
            start_Index = 14
            self.velocity_x = 4

         # 방향이 오른쪽이면, 오른쪽 이미지 선택
        if self.direction == 'right':
            self.images = self.images_right
        # 방향이 왼쪽이면 왼쪽 이미지 선택, 진행방향 x축으로 -
        elif self.direction == 'left':
            self.images = self.images_left
            self.velocity_x = abs(self.velocity_x) * -1
         
       
 
        # loop 시간 더하기
        self.current_time += mt

        # loop time 경과가 animation_time을 넘어서면 새로운 이미지 출력 
        if self.current_time >= self.animation_time:
            self.current_time = 0

            # 상태에 따라 이미지 index 범위를 다르게 설정한다.
            # idle 상태는 0 ~ 9, 걷기 상태는 10 ~ 19
            self.index = (self.index % count) + start_Index
           
            self.image = self.images[self.index]
            self.index += 1

            if self.index >= len(self.images):
                self.index = 0
        
 
           
 
 