class Robot:

    def __init__(self, position=(0,0), heading=0):
        self.position = position
        self.heading = heading

        print("Initialize robot at (" + str(self.position[0]) + ", " + str(self.position[1]) + ", " + str(self.heading) + ")")

    def rotate(self, ang_x):

        self.heading += ang_x * dt

    def translate(self, vel_x, vel_y):

        pos_x = self.position[0] + vel_x * dt
        pos_y = self.position[1] + vel_y * dt