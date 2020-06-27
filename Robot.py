from math import *

class Robot:

    def __init__(self, position=[0,0], heading=0, dt = 0.1):
        self.position = position
        self.heading = heading
        self.dt = dt
        self.tolerance = 5

        print("Initialize robot at (" + str(self.position[0]) + ", " + str(self.position[1]) + ", " + str(self.heading) + ")")

    def rotate(self, ang_x):

        if(self.heading>2*pi):
            self.heading=0

        self.heading += ang_x * self.dt

    def translate(self, vel):

        self.position[0] += vel * self.dt * cos(self.heading)
        self.position[1] += vel * self.dt * sin(self.heading)

    def set_goal(self, goal):
        self.goal = goal

        dx = self.goal[0] - self.position[0]
        dy = self.goal[1] - self.position[1]

        self.heading_target = atan2(dy, dx)
        print("Set robot goal at: " + str(goal) + ", direction: " + str(self.heading_target))

    def control(self, kp_ang):

        if(self.heading != self.heading_target):
            heading_diff = self.heading_target - self.heading

            self.rotate = (heading_diff * kp_ang)

    def is_directed(self):
        tolerance = 0.01
        heading_diff = self.heading_difference()

        if (heading_diff < tolerance and heading_diff > -tolerance):
            return True
        else: return False

    def is_at_goal(self):

        if (self.distance_to_goal() < self.tolerance):
            return True
        else: return False

    def heading_difference(self):
        return self.heading_target - self.heading

    def distance_to_goal(self):
        dx = self.goal[0] - self.position[0]
        dy = self.goal[1] - self.position[1]

        return sqrt(dx**2 + dy**2)

    