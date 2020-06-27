class Robot:

    def __init__(self, position=[0,0], heading=0, dt = 0.1):
        self.position = position
        self.heading = heading
        self.dt = dt

        print("Initialize robot at (" + str(self.position[0]) + ", " + str(self.position[1]) + ", " + str(self.heading) + ")")

    def rotate(self, ang_x):

        self.heading += ang_x * self.dt

    def translate(self, vel_x, vel_y):

        pos_x = self.position[0] + vel_x * self.dt
        pos_y = self.position[1] + vel_y * self.dt

        self.position = (pos_x, pos_y)