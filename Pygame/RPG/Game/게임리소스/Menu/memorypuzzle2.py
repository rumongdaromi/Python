import random, pygame, sys
from pygame.locals import *
from abc import *

FPS = 30 # frames per second, the general speed of the program
WINDOWWIDTH = 640 # size of window's width in pixels
WINDOWHEIGHT = 480 # size of windows' height in pixels
GAPSIZE = 10 # size of gap between boxes in pixels

#            R    G    B
GRAY     = (100, 100, 100)
NAVYBLUE = ( 60,  60, 100)
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (255,   0, 255)
CYAN     = (  0, 255, 255)

BGCOLOR = NAVYBLUE
LIGHTBGCOLOR = GRAY
BOXCOLOR = WHITE
HIGHLIGHTCOLOR = BLUE

DONUT = 0
SQUARE = 1
DIAMOND = 2
LINES = 3
OVAL = 4

class Box(object):
    size = 40
    quarter = int(size * 0.25)
    half = int(size * 0.5)
    fps_clock = None
    surf = None
    
    def __init__(self, color, shape):
        self.color = color
        self.shape = shape
        self.state = False # cover가 닫혔으면 False, 열렸으면 True

    def set_coord(self, x, y):
        self.coord = (x, y)
        self.rect = pygame.Rect(x, y, self.size, self.size)

    def draw_shape(self):
        f = (self.draw_donut, self.draw_square, self.draw_diamond, self.draw_lines, self.draw_oval)
        f[self.shape](self.coord[0], self.coord[1])

    def draw_donut(self, x, y):
        pygame.draw.circle(self.surf, self.color, (x + self.half, y + self.half), self.half - 5)
        pygame.draw.circle(self.surf, BGCOLOR, (x + self.half, y + self.half), self.quarter - 5)
        
    def draw_square(self, x, y):
        pygame.draw.rect(self.surf, self.color, (x + self.quarter, y + self.quarter, self.size - self.half, self.size - self.half))

    def draw_diamond(self, x, y):
        q, h = self.quarter, self.half
        pygame.draw.polygon(self.surf, self.color, ((x + h, y), (x + self.size - 1, y + h), (x + h, y + self.size - 1), (x, y + h)))

    def draw_lines(self, x, y):
        for i in range(0, self.size, 4):
            pygame.draw.line(self.surf, self.color, (x, y + i), (x + i, y))
            pygame.draw.line(self.surf, self.color, (x + i, y + self.size - 1), (x + self.size - 1, y + i))

    def draw_oval(self, x, y):
        pygame.draw.ellipse(self.surf, self.color, (x, y + self.quarter, self.size, self.half))

    def draw_cover(self):
        pygame.draw.rect(self.surf, BOXCOLOR, (self.coord[0], self.coord[1], self.size, self.size))

    def draw_highlight(self):
        x, y = self.coord
        pygame.draw.rect(self.surf, HIGHLIGHTCOLOR, (x - 5, y - 5, self.size + 10, self.size + 10), 4)

    def compare(self, box):
        return (self.shape == box.shape and self.color == box.color)

    def draw_cover_animation(self, boxes, width):
        for box in boxes:
            pygame.draw.rect(Box.surf, BGCOLOR, (box.coord[0], box.coord[1], box.size, box.size))
            box.draw_shape()
            if width > 0:
                pygame.draw.rect(Box.surf, BOXCOLOR, (box.coord[0], box.coord[1], width, box.size))
        pygame.display.update()
        self.fps_clock.tick(FPS)


class Game(object):
    def __init__(self, diff):
        self.set_data(diff)
        Box.quarter = int(Box.size * 0.25)
        Box.half = int(Box.size * 0.5)
        self.boxes = []

        Box.surf.fill(BGCOLOR)
        self.make_boxes()
        self.init_game()

    def init_game(self):
        self.cur_box = None
        self.first_box = None
        self.start_animation()

    def run_game(self):
        while True:
            mouse_clicked = False

            Box.surf.fill(BGCOLOR)
            self.draw_boxes()

            for e in pygame.event.get():
                if e.type == QUIT or (e.type == KEYUP and e.key == K_ESCAPE):
                    return
                elif e.type == MOUSEMOTION:
                    self.cur_box = self.get_box(e.pos)
                elif e.type == MOUSEBUTTONUP:
                    self.cur_box = self.get_box(e.pos)
                    mouse_clicked = True

            if self.cur_box != None:
                if not self.cur_box.state:
                    self.cur_box.draw_highlight()
                if not self.cur_box.state and mouse_clicked:
                    self.open_animation([self.cur_box])
                    self.cur_box.state = True
                    if self.first_box == None:
                        self.first_box = self.cur_box
                    else:
                        if not self.first_box.compare(self.cur_box):
                            pygame.time.wait(1000)
                            self.close_animation([self.first_box, self.cur_box])
                            self.first_box.state = False
                            self.cur_box.state = False
                        elif self.has_won():
                            self.won_animation()
                            pygame.time.wait(1000)
                            return
                        self.first_box = None        
                
            pygame.display.update()
            Box.fps_clock.tick(FPS)
    
    def make_boxes(self):
        colors = [RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN]
        shapes = (DONUT, SQUARE, DIAMOND, LINES, OVAL)
        assert len(colors) * len(shapes) * 2 >= self.width * self.height, "Board is too big for the number of shapes/colors defined."
        XMARGIN = int((WINDOWWIDTH - (self.width * (Box.size + GAPSIZE))) / 2)
        YMARGIN = int((WINDOWHEIGHT - (self.height * (Box.size + GAPSIZE))) / 2)

        numBoxesUsed = int(self.width * self.height / 2) # calculate how many icons are needed
        random.shuffle(colors)
        for color in colors:
            for shape in shapes:
                if len(self.boxes) < numBoxesUsed * 2:
                    self.boxes.append(Box(color, shape))
                    self.boxes.append(Box(color, shape))
                
        random.shuffle(self.boxes)
        for i in range(len(self.boxes)):
            x = XMARGIN + GAPSIZE // 2 + (Box.size + GAPSIZE) * (i % self.width)
            y = YMARGIN + GAPSIZE // 2 + (Box.size + GAPSIZE) * (i // self.width)
            self.boxes[i].set_coord(x, y)
    
    def make_groups(self, size, num_list):
        result = []
        for i in range(0, len(num_list), size):
            group = []
            for j in range(size):
                if i + j < len(num_list):
                    group.append(self.boxes[num_list[i + j]])
                else:
                    break
            result.append(group)
        return result

    def close_animation(self, group):
        for coverage in range(0, group[0].size + self.open_speed, self.open_speed):
            group[0].draw_cover_animation(group, coverage)

    def open_animation(self, group):
        for coverage in range(group[0].size, -1, -self.open_speed):
            group[0].draw_cover_animation(group, coverage)

    def start_animation(self):
        numofboxes = [x for x in range(len(self.boxes))]
        random.shuffle(numofboxes)
        box_groups = self.make_groups(self.split_size, numofboxes)

        self.draw_boxes()
        for group in box_groups:
            self.open_animation(group)
            self.close_animation(group)

    def get_box(self, pos):
        for box in self.boxes:
            if box.rect.collidepoint(pos):
                return box
        return None

    def won_animation(self):
        color1 = LIGHTBGCOLOR
        color2 = BGCOLOR

        for i in range(13):
            color1, color2 = color2, color1
            Box.surf.fill(color1)
            self.draw_boxes()
            pygame.display.update()
            pygame.time.wait(300)

    def has_won(self):
        for box in self.boxes:
            if not box.state:
                return False
        return True

    def draw_boxes(self):
        for box in self.boxes:
            if box.state:
                box.draw_shape()
            else:
                box.draw_cover()

    def set_data(self, diff):
        if diff == 'Easy':
            Box.size = 80
            Game.width = 5
            Game.height = 4
            self.split_size = 3
            self.open_speed = 10
            
        elif diff == 'Normal':
            Box.size = 70
            Game.width = 6
            Game.height = 5
            self.split_size = 5
            self.open_speed = 10

        elif diff == 'Hard':
            Box.size = 60
            Game.width = 8
            Game.height = 6
            self.split_size = 7
            self.open_speed = 10
        
        elif diff == 'Very Hard':
            Box.size = 48
            self.width = 10
            self.height = 7
            self.split_size = 8
            self.open_speed = 8


class Menu(object):
    def __init__(self):
        self.menu_width = 400
        self.menu_height = 300
        self.left = WINDOWWIDTH / 2 - self.menu_width / 2
        self.top = WINDOWHEIGHT / 2 - self.menu_height / 2
        self.menubox_color = GRAY
        self.y = self.top + 35
        self.menu_items = ('Memory Puzzle Game', 'Easy', 'Normal', 'Hard', 'Very Hard')
        self.menu_rects = []

        pygame.init()
        Box.fps_clock = pygame.time.Clock()
        Box.surf = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
        pygame.display.set_caption('Memory Puzzle')
        self.font = pygame.font.Font('freesansbold.ttf', 30)

        Box.surf.fill(BGCOLOR)
        self.draw_menubox()
        for menu in self.menu_items:
            rect = self.draw_menu(menu, self.y)
            self.menu_rects.append(rect)
            self.y += 55
        pygame.display.update()

    def get_menu(self):            
        while True:
            for e in pygame.event.get():
                if e.type == QUIT or (e.type == KEYUP and e.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                elif e.type == MOUSEBUTTONUP:
                    index = self.find_menu(e.pos)
                    if index:
                        return index
        Box.fps_clock.tick(FPS)

    def find_menu(self, pos):
        for x in range(1, len(self.menu_rects)):
            if self.menu_rects[x].collidepoint(pos):
                return x
        return 0
                    
    def make_text(self, text, x, y):
        surf = self.font.render(text, True, ORANGE)
        rect = surf.get_rect()
        rect.center = (x, y)
        Box.surf.blit(surf, rect)
        return rect

    def draw_menu(self, text, y):
        x = WINDOWWIDTH / 2
        return self.make_text(text, x, y)

    def draw_menubox(self):
        pygame.draw.rect(Box.surf, self.menubox_color, (self.left, self.top, self.menu_width, self.menu_height))
   
    
if __name__ == '__main__':
    while True:
        menu = Menu()
        diff = menu.menu_items[menu.get_menu()]
        game = Game(diff)
        game.run_game()
