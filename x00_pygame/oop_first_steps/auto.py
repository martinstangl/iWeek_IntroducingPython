import random


class Auto:
    def __init__(self, speed, tank, fahrbereit=True):
        self.color = (random.randint(0, 255),
                      random.randint(0, 255),
                      random.randint(0, 255))
        self.speed = speed
        self.tank = tank
        self.fahrbereit = fahrbereit
        self.pos = [0, 0]

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

