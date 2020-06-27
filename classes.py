import math
import random
import pygame
from consts import *


def collide(obj1, obj2):
    if obj1.r + obj2.r < math.sqrt((obj1.x - obj2.x) ** 2 + (obj1.y - obj2.y) ** 2):
        return False
    else:
        return True


def init_menu_buttons():
    button1 = Button(*BUTTON1, random.randint(0, 255), 'play')
    button2 = Button(*BUTTON2, random.randint(0, 255), 'exit')
    return [button1, button2]


def init_menu_circles():
    circles = []
    for i in range(30):
        circles.append(Circle(random.randint(0, WINDOW_SIZEX), random.randint(0, WINDOW_SIZEY), random.randint(20, 50), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 'menu'))
    return circles


def init_game_circles():
    circles = []
    for i in range(10):
        circles.append(Circle(random.randint(0, WINDOW_SIZEX), random.randint(-WINDOW_SIZEY, 0), 10, GREEN, 'game'))
    for i in range(90):
        circles.append(Circle(random.randint(0, WINDOW_SIZEX), random.randint(-WINDOW_SIZEY, 0), 10, BLACK, 'game'))
    return circles


class Button:
    def __init__(self, coords, sizex, sizey, color, text):
        self.delta = 0
        self.coords = coords
        self.sizex = sizex
        self.sizey = sizey
        self.color = color
        self.text = text
        self.shrift = pygame.font.SysFont('arial', 30).render(self.text, 0, WHITE)
        self.button = pygame.Rect(self.coords[0] - self.delta, self.coords[1] - self.delta, self.sizex + 2*self.delta, self.sizey + 2*self.delta)

    def update(self):
        self.button = pygame.Rect(self.coords[0] - self.delta, self.coords[1] - self.delta, self.sizex + 2*self.delta, self.sizey + 2*self.delta)

    def draw(self, surface):
        pygame.draw.ellipse(surface, self.color, self.button)
        surface.blit(self.shrift, (self.coords[0] + 2*self.sizex//5, self.coords[1]))


class Menu:
    def __init__(self, buttons, circles):
        self.buttons = buttons
        self.circles = circles

    def check_mouse_pos(self):
        for i in self.buttons:
            if i.button.collidepoint(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                return i

    def draw_animation(self, circles, surface):
        for i in circles:
            i.draw(surface)

    def draw(self, surface):
        for i in self.buttons:
            i.draw(surface)


class Circle:
    def __init__(self, x, y, r, color, type):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.type = type

    def move(self):
        if self.y - self.r <= WINDOW_SIZEY:
            self.y += 10
        else:
            if self.type == 'menu':
                self.menu_randomize()
            if self.type == 'game':
                self.game_randomize()

    def menu_randomize(self):
        self.x = random.randint(0, WINDOW_SIZEX)
        self.y = random.randint(0, WINDOW_SIZEY)
        self.r = random.randint(20, 50)

    def game_randomize(self):
        self.x = random.randint(0, WINDOW_SIZEX)
        self.y = random.randint(-WINDOW_SIZEY, 0)

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.r)


class Player(Circle):
    def __init__(self, x, y, r, color, type):
        super().__init__(x, y, r, color, type)
        self.life_COUNT = 1
        self.dir = None
        self.rect = pygame.Rect(x - r, y - r, 2 * r, 2 * r)

    def move(self):
        if self.dir == 'wd':
            self.x += 15
            self.y -= 15
        if self.dir == 'ds':
            self.x += 15
            self.y += 15
        if self.dir == 'sa':
            self.x -= 15
            self.y += 15
        if self.dir == 'aw':
            self.x -= 15
            self.y -= 15
        if self.dir == 'w':
            self.y -= 15
        if self.dir == 'd':
            self.x += 15
        if self.dir == 's':
            self.y += 15
        if self.dir == 'a':
            self.x -= 15

    def check_position(self):
        if self.x < 0:
            self.x = 0
        if self.y < 0:
            self.y = 0
        if self.x > WINDOW_SIZEX:
            self.x = WINDOW_SIZEX
        if self.y > WINDOW_SIZEY:
            self.y = WINDOW_SIZEY


class Interface:
    def __init__(self, x, y, r, life_count):
        self.x = x
        self.y = y
        self.r = r
        self.life_count = life_count
        self.text = pygame.font.SysFont('arial', 20).render('X' + str(self.life_count), 0, BLACK)
        self.life = Circle(self.x + self.r + 10, self.y, 10, GREEN, '')

    def draw(self, surface):
        surface.blit(self.text, (self.x + 2 * self.r, self.y - self.r//2))
        self.life.draw(surface)