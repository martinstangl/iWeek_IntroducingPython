class Auto:
    def __init__(self, c, speed, tank, fahrbereit=True):
        self.color = c
        self.speed = speed
        self.tank = tank
        self.fahrbereit = fahrbereit

    def acc(self, a):
        self.speed += a

    def move(self):
        if self.fahrbereit:
            pass

    def output(self):
        print("Farbe:",self.color,"Speed:",self.speed,"Tank:",self.tank)




    # def set_color(self,rw,gw,bw):
    #     if 0 <= rw <= 255:
    #         pass

