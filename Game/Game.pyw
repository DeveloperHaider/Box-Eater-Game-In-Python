import pygame
import sys
import random


class Game:

    def __init__(self):
        pygame.init()
        self.title = "Box Eater"
        self.icon = "icon.bmp"
        self.height = 800
        self.width = 620
        self.quit = 0
        self.background = (255, 255, 255)
        self.not_quit = 1
        self.speed = 20
        self.delay = 75
        self.start()

    def start(self):
        pygame.display.set_mode((self.height, self.width))
        pygame.mouse.set_visible(0)
        pygame.display.set_caption(self.title)
        pygame.display.set_icon(pygame.image.load(self.icon))
        screen = pygame.display.get_surface()
        display = Display()
        player = Player()
        obj = Obj()
        screen.fill(self.background)
        display.show_msg()
        while self.not_quit:
            display.clock.tick(display.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == 27):
                    self.not_quit = 0
                if ((event.type == pygame.KEYDOWN) and (event.key == 273)) and player.do_move_up == 1:
                    player.move_up()
                if ((event.type == pygame.KEYDOWN) and (event.key == 274)) and player.do_move_down == 1:
                    player.move_down()
                if ((event.type == pygame.KEYDOWN) and (event.key == 275)) and player.do_move_left == 1:
                    player.move_left()
                if ((event.type == pygame.KEYDOWN) and (event.key == 276)) and player.do_move_right == 1:
                    player.move_right()
            screen.fill(self.background)
            display.show_border()
            obj.generate()
            player.show()
            if player._move_up:
                player.y -= self.speed
            if player._move_down:
                player.y += self.speed
            if player._move_left:
                player.x += self.speed
            if player._move_right:
                player.x -= self.speed
            if ((obj.x == player.x) and (obj.y == player.y)) or ((obj.x+20 == player.x) and (obj.y == player.y))\
                    or ((obj.x-20 == player.x) and (obj.y == player.y))\
                    or ((obj.x == player.x) and (obj.y+20 == player.y))\
                    or ((obj.x == player.x) and (obj.y-20 == player.y)):
                obj.do_generate = 1
                display.add_point()
            if player.y == 20:
                player.move_down()
            if player.y == 540:
                player.move_up()
            if player.x == 20:
                player.move_left()
            if player.x == 740:
                player.move_right()
            display.show_point()
            pygame.display.update()
            pygame.time.delay(self.delay)
        self.stop()

    def stop(self):
        if not self.not_quit:
            display = Display()
            display.msg = "Goodbye"
            display.delay = 1000
            display.show_msg()
            pygame.quit()
            sys.exit()


class Display:

    def __init__(self):
        self.msg = 'Welcome'
        self.font_size = 80
        self.font = None
        self.delay = 3000
        self.mode = 0
        self.point = 0
        self.fps = 60
        self.clock = pygame.time.Clock()

    def show_border(self):
        screen = pygame.display.get_surface()
        self.mode = 1
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(20, 20, 760, 560), self.mode)

    def show_msg(self):
        screen = pygame.display.get_surface()
        fg = (255, 0, 0)
        bg = (255, 255, 255)
        font = pygame.font.Font(self.font, self.font_size)
        font_x, font_y = font.size(self.msg)
        ren = font.render(self.msg, 1, fg, bg)
        screen.blit(ren, (400-(font_x/2), 310-(font_y/2)))
        pygame.display.update()
        pygame.time.delay(self.delay)

    def show_point(self):
        screen = pygame.display.get_surface()
        fg = (255, 0, 0)
        bg = (255, 255, 255)
        self.font_size = 30
        self.msg = 'Score : '+str(self.point)+' Points'
        font = pygame.font.Font(self.font, self.font_size)
        font_x, font_y = font.size(self.msg)
        ren = font.render(self.msg, 1, fg, bg)
        screen.blit(ren, (400-(font_x/2), 605-(font_y/2)))

    def add_point(self):
        self.point = (self.point + 1)


class Player:

    def __init__(self):
        self.size = 40
        self.clr = (0, 0, 255)
        self.x, self.y = 380, 280
        self.do_move_up = 1
        self.do_move_down = 1
        self.do_move_left = 1
        self.do_move_right = 1
        self._move_up = 1
        self._move_down = 0
        self._move_left = 0
        self._move_right = 0

    def show(self):
        screen = pygame.display.get_surface()
        self.x, self.y, h, w = pygame.draw.rect(screen, self.clr, pygame.Rect(self.x, self.y, self.size, self.size), 0)

    def move_up(self):
        self._move_up = 1
        self._move_down = 0
        self._move_left = 0
        self._move_right = 0

    def move_down(self):
        self._move_up = 0
        self._move_down = 1
        self._move_left = 0
        self._move_right = 0

    def move_left(self):
        self._move_up = 0
        self._move_down = 0
        self._move_left = 1
        self._move_right = 0

    def move_right(self):
        self._move_up = 0
        self._move_down = 0
        self._move_left = 0
        self._move_right = 1


class Obj:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.clr = (255, 0, 0)
        self.do_generate = 1

    def generate(self):
        screen = pygame.display.get_surface()
        if self.do_generate == 1:
            self.x = random.randrange(20, 750, 20)
            self.y = random.randrange(20, 550, 20)
            self.x, self.y, box_h, box_w = pygame.draw.rect(screen, self.clr, pygame.Rect(self.x, self.y, 40, 40), 0)
            self.do_generate = 0
        else:
            self.x, self.y, box_h, box_w = pygame.draw.rect(screen, self.clr, pygame.Rect(self.x, self.y, 40, 40), 0)
            self.do_generate = 0

if __name__ == '__main__':
    Game()
