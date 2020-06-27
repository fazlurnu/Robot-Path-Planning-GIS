from Robot import Robot
import pygame

WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255, 0, 0)
GREEN=(0,255,0)
BLUE=(0,0,255)

class Display:

    def __init__(self, robot):

        self.height = 500
        self.width = 500

        caption = 'Python Code for Robot Command'
        pygame.init()
        print("Initialize PyGame Display, Caption: " + caption + ", size: " + str(self.width) + "x" + str(self.height))
        pygame.display.set_caption(caption)
        self.screen = pygame.display.set_mode((self.width, self.height))

        self.screen.fill(WHITE)

        border_width = 5

        self.draw_robot(robot)
        
        self.display()

    def draw_robot(self, robot):
        pos_x = robot.position[0]
        pos_y = robot.position[1]

        pygame.draw.circle(self.screen, RED, [pos_x, pos_y], 10)

    def display(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # If user clicked close
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
