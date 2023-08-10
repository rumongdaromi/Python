import pygame
import sys

# 스크린 전체 크기 지정
SCREEN_WIDTH = 1020
SCREEN_HEIGHT = 900  #바닥을 보게해줌
 
# pygame 초기화
pygame.init()
 
# 스크린 객체 저장
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("pygame Sprite")
 
# FPS를 위한 Clock 생성
clock = pygame.time.Clock()
FPS = 60

# 속도와 질량 기본 값
VELOCITY = 8 #점프
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
        animation_size = 22
        # 여러장의 이미지를 리스트로 저장한다. 이미지 경로는 자신들의 경로를 사용한다.
        images = []
        # 서있는 상태 0 ~ 9
        images.append(pygame.image.load('/Users/imin-ug/Python/게임프로그래밍/파이게임/겜프프로젝트/진짜제출폴더임/유저 케릭터 파일/outImgs-4/0.png'))
        images.append(pygame.image.load('/Users/imin-ug/Python/게임프로그래밍/파이게임/겜프프로젝트/진짜제출폴더임/유저 케릭터 파일/outImgs-4/1.png'))
        images.append(pygame.image.load('/Users/imin-ug/Python/게임프로그래밍/파이게임/겜프프로젝트/진짜제출폴더임/유저 케릭터 파일/outImgs-4/2.png'))
        images.append(pygame.image.load('/Users/imin-ug/Python/게임프로그래밍/파이게임/겜프프로젝트/진짜제출폴더임/유저 케릭터 파일/outImgs-4/3.png'))
        images.append(pygame.image.load('/Users/imin-ug/Python/게임프로그래밍/파이게임/겜프프로젝트/진짜제출폴더임/유저 케릭터 파일/outImgs-4/4.png'))
        images.append(pygame.image.load('/Users/imin-ug/Python/게임프로그래밍/파이게임/겜프프로젝트/진짜제출폴더임/유저 케릭터 파일/outImgs-4/5.png'))
        images.append(pygame.image.load('/Users/imin-ug/Python/게임프로그래밍/파이게임/겜프프로젝트/진짜제출폴더임/유저 케릭터 파일/outImgs-4/6.png'))
        images.append(pygame.image.load('/Users/imin-ug/Python/게임프로그래밍/파이게임/겜프프로젝트/진짜제출폴더임/유저 케릭터 파일/outImgs-4/7.png'))
        images.append(pygame.image.load('/Users/imin-ug/Python/게임프로그래밍/파이게임/겜프프로젝트/진짜제출폴더임/유저 케릭터 파일/outImgs-4/8.png'))
        images.append(pygame.image.load('/Users/imin-ug/Python/게임프로그래밍/파이게임/겜프프로젝트/진짜제출폴더임/유저 케릭터 파일/outImgs-4/9.png'))
        # 걷기 10 ~ 16
        images.append(pygame.image.load('/Users/imin-ug/Python/게임프로그래밍/파이게임/겜프프로젝트/진짜제출폴더임/유저 케릭터 파일/outImgs-3/0.png'))
        images.append(pygame.image.load('/Users/imin-ug/Python/게임프로그래밍/파이게임/겜프프로젝트/진짜제출폴더임/유저 케릭터 파일/outImgs-3/1.png'))
        images.append(pygame.image.load('/Users/imin-ug/Python/게임프로그래밍/파이게임/겜프프로젝트/진짜제출폴더임/유저 케릭터 파일/outImgs-3/2.png'))
        images.append(pygame.image.load('/Users/imin-ug/Python/게임프로그래밍/파이게임/겜프프로젝트/진짜제출폴더임/유저 케릭터 파일/outImgs-3/3.png'))
        images.append(pygame.image.load('/Users/imin-ug/Python/게임프로그래밍/파이게임/겜프프로젝트/진짜제출폴더임/유저 케릭터 파일/outImgs-3/4.png'))
        images.append(pygame.image.load('/Users/imin-ug/Python/게임프로그래밍/파이게임/겜프프로젝트/진짜제출폴더임/유저 케릭터 파일/outImgs-3/5.png'))
        images.append(pygame.image.load('/Users/imin-ug/Python/게임프로그래밍/파이게임/겜프프로젝트/진짜제출폴더임/유저 케릭터 파일/outImgs-3/6.png'))
        # 공격 17~22
        images.append(pygame.image.load('/Users/imin-ug/Python/게임프로그래밍/파이게임/겜프프로젝트/진짜제출폴더임/유저 케릭터 파일/outImgs-5/0.png'))
        images.append(pygame.image.load('/Users/imin-ug/Python/게임프로그래밍/파이게임/겜프프로젝트/진짜제출폴더임/유저 케릭터 파일/outImgs-5/1.png'))
        images.append(pygame.image.load('/Users/imin-ug/Python/게임프로그래밍/파이게임/겜프프로젝트/진짜제출폴더임/유저 케릭터 파일/outImgs-5/2.png'))
        images.append(pygame.image.load('/Users/imin-ug/Python/게임프로그래밍/파이게임/겜프프로젝트/진짜제출폴더임/유저 케릭터 파일/outImgs-5/3.png'))
        images.append(pygame.image.load('/Users/imin-ug/Python/게임프로그래밍/파이게임/겜프프로젝트/진짜제출폴더임/유저 케릭터 파일/outImgs-5/4.png'))
        images.append(pygame.image.load('/Users/imin-ug/Python/게임프로그래밍/파이게임/겜프프로젝트/진짜제출폴더임/유저 케릭터 파일/outImgs-5/5.png'))

        ememy =  pygame.image.load("/Users/imin-ug/Python/게임프로그래밍/파이게임/겜프프로젝트/게임리소스/c1.png")
 
        # rect 만들기
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
        # loop 시간 더하기
         
        self.current_time += mt
        # isJump 값이 0보다 큰지 확인
        if self.isJump > 0:
            # isJump 값이 2일 경우 속도를 리셋
            # 점프 한 상태에서 다시 점프를 위한 값
            # 이 코드를 주석처리하면 이중점프를 못한다.
            #if self.isJump == 2:
            #     self.v = VELOCITY
 
            # 역학공식 계산 (F). F = 0.5 * mass * velocity^2.
            if self.v > 0:
                # 속도가 0보다 클때는 위로 올라감
                F = (0.5 * self.m * (self.v * self.v))
            else:
                # 속도가 0보다 작을때는 아래로 내려감
                F = -(0.5 * self.m * (self.v * self.v))
 
            # 좌표 수정 : 위로 올라가기 위해서는 y 좌표를 줄여준다.
            self.rect.y -= round(F)
 
            # 속도 줄여줌
            self.v -= 1
 
            # 바닥에 닿았을때, 변수 리셋
            if self.rect.bottom > SCREEN_HEIGHT:
                self.rect.bottom = SCREEN_HEIGHT
                self.isJump = 0
                self.v = VELOCITY
        
        
        
        
        # update를 통해 캐릭터의 이미지가 계속 반복해서 나타나도록 한다.
       
        # 현재 상태에 따라 반복해줄 이미지의 index 설정과 속도
        if self.state == 0:
            count = 10 #플레이어 이미지의 갯수와 동일해야함
            start_Index = 0
            self.velocity_x = 0
        elif self.state == 1:
            count = 7
            start_Index = 10
            self.velocity_x = 4 #플레이어속도
            
        elif self.state == 2:
                self.velocity_x = 0
                count = 6
                start_Index = 17
                self.index+= 1
                if self.index >= 22:
                    self.index = 0
                                               
        # 방향이 오른쪽이면, 오른쪽 이미지 선택
        if self.direction == 'right':
            self.images = self.images_right
        # 방향이 왼쪽이면 왼쪽 이미지 선택, 진행방향 x축으로 -
        elif self.direction == 'left':
            self.images = self.images_left
            self.velocity_x = abs(self.velocity_x) * -1
         
        # loop time 경과가 animation_time을 넘어서면 새로운 이미지 출력 
        if self.current_time >= self.animation_time:
            self.current_time = 0

            # 상태에 따라 이미지 index 범위를 다르게 설정한다.
            # idle 상태 = 0 ~ 10, 걷기 상태는 11 ~ 17  공격상태 18~23
            #count = 6   start_Index = 17  17~22
            self.index = (self.index % count) + start_Index
            self.image = self.images[self.index]
            self.index += 1
            print(self.index)
            if self.index >= len(self.images):
                self.index = 0
            # 좌우 위치값 변경, 이동
        self.rect.x += self.velocity_x
 
 
