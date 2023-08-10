import sys
import pygame
from pygame.locals import QUIT, Rect, KEYDOWN, K_SPACE

class Cvar:
     
    def __init__(self,user_x,is_left_arrow = False,is_space_down = False,is_right_arrow = False):
        self.is_left_arrow = is_left_arrow
        self.is_space_down = is_space_down
        self.is_right_arrow = is_right_arrow
        self.user_x = user_x
    def move(self):
        self.user_x += 6
        return self.user_x

                    
                    
                    
                    
                    
                    
