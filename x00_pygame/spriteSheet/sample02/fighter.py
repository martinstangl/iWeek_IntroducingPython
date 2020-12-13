import pygame

from sample02.spritesheets import SpriteSheet


class Fighter:
    def __init__(self, pos, screen_width, screen_height, x_transform=False):
        self.pos = pos
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.walkStop = []
        self.walkRight = []
        self.walkLeft = []
        self.walkKick = []
        self.walkJumpRight = []
        #self.kick = {"weak": []}
        self.walkPunch = {"weak": []}
        self.ss = SpriteSheet('./img/ken.png')
        self.init_pics(x_transform)
        self.left = False
        self.right = False
        self.standing = True
        self.punch = False
        self.kick = False
        self.walkCount = 0
        self.jump = False
        self.jumpCount = 7

    def init_pics(self, x_transform):
        self.walkStop = self.ss.images_at([(1, 1, 43, 75),
                                           (44, 1, 43, 75),
                                           (88, 1, 43, 75),
                                           (128, 1, 43, 75),
                                           (88, 1, 43, 75),
                                           (44, 1, 43, 75),
                                           (1, 1, 43, 75)], colorkey=(168, 136, 168), x_transform=x_transform)
        self.image_scaler(self.walkStop)
        self.walkJumpRight = self.ss.images_at([(251, 482, 35, 70),
                                                (288, 467, 35, 75),
                                                (321, 467, 59, 40),
                                                (381, 446, 35, 65),
                                                (413, 467, 70, 40),
                                                (484, 453, 43, 70),
                                                (530, 466, 32, 85),
                                                (251, 482, 35, 70)], colorkey=(168, 136, 168), x_transform=x_transform)
        self.image_scaler(self.walkJumpRight)

       # self.punch["weak"] = self.ss.load_strip((255, 40, 47, 75), 3, colorkey=(168, 136, 168))
        self.walkPunch["weak"] = self.ss.images_at([(255, 40, 42, 70),
                                               (302, 40, 50, 70),
                                               (351, 40, 42, 70)], colorkey=(168, 136, 168), x_transform=x_transform)
        self.image_scaler(self.walkPunch["weak"])

        self.walkKick = self.ss.images_at([(255, 153, 40, 75),
                                           (293, 153, 40, 75),
                                           (335, 153, 63, 75),
                                           (400, 153, 40, 75),
                                           (447, 153, 40, 75),
                                           ], colorkey=(168, 136, 168), x_transform=x_transform)
        self.image_scaler(self.walkKick)

        self.walkRight = self.ss.load_strip((1, 75, 43, 75), 5, colorkey=(168, 136, 168), x_transform=x_transform)
        self.image_scaler(self.walkRight)
        self.walkLeft = self.ss.load_strip((1, 75, 43, 75), 5, colorkey=(168, 136, 168), x_transform=x_transform)
        self.image_scaler(self.walkLeft)

    def move(self):
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.pos[0] -= 1
            self.left = True
            self.right = False
            self.standing = False
            self.kick = False
        elif pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.pos[0] += 1
            self.left = False
            self.right = True
            self.standing = False
            self.kick = False
        elif pygame.key.get_pressed()[pygame.KMOD_LALT]:
            pass
        else:
            self.left = False
            self.right = False
            self.standing = True

        self.check_punch()
        self.check_kick()
        self.check_jump()

    def check_punch(self):
        if not self.punch:
            if pygame.key.get_pressed()[pygame.K_p]:
                self.punch = True
                self.left = False
                self.right = False
                self.standing = False
                self.kick = False
                self.walkCount = 0
        else:
            if self.walkCount == 12:
                self.punch = False
                self.standing = True

    def check_kick(self):
        if not self.kick:
            if pygame.key.get_pressed()[pygame.K_k]:
                self.punch = False
                self.left = False
                self.right = False
                self.standing = False
                self.kick = True
                self.walkCount = 0
        else:
            if self.walkCount == 14:
                self.kick = False
                self.standing = True
                self.walkCount = 0

    def check_jump(self):
        if not self.jump:
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                self.jump = True
                self.punch = False
                self.left = False
                self.right = False
                self.standing = False
                self.kick = False
                self.walkCount = 0
        else:
            if self.jumpCount >= -7:
                self.pos[1] -= (self.jumpCount * abs(self.jumpCount)) * 0.5
                self.pos[0] += 2
                self.jumpCount -= 1
            else:
                self.jumpCount = 7
                self.jump = False

    def draw_images(self, display, images):
        for i in range(len(images)):
            display.blit(images[i], (self.screen_width/2, i*75))

    @staticmethod
    def image_scaler(images):
        for i in range(len(images)):
            images[i] = pygame.transform.scale2x(images[i])

    def draw(self, display):

        if self.walkCount + 1 >= 100:
            self.walkCount = 0
        if self.left:
            display.blit(self.walkLeft[(self.walkCount // 3) % 5], (self.pos[0], self.pos[1]))
            self.walkCount += 1
        elif self.right:
            display.blit(self.walkRight[(self.walkCount // 3) % 5], (self.pos[0], self.pos[1]))
            self.walkCount += 1
        elif self.punch:
            display.blit(self.walkPunch["weak"][(self.walkCount // 3) % 3], (self.pos[0], self.pos[1]))
            self.walkCount += 1
        elif self.kick:
            display.blit(self.walkKick[(self.walkCount//3) % 5], (self.pos[0], self.pos[1]))
            self.walkCount += 1
        elif self.jump:
            display.blit(self.walkJumpRight[(self.walkCount // 3) % 8], (self.pos[0], self.pos[1]))
            self.walkCount += 1
            olist = pygame.mask.from_surface(self.walkJumpRight[(self.walkCount // 3) % 3]).outline()
            pygame.draw.lines(display, (200, 150, 150), 1, olist)

        else:
            #self.draw_images(display, self.walkPunch["weak"])

            #print(self.standing)
            #print(self.pos[0])

            olist = pygame.mask.from_surface(self.walkStop[(self.walkCount // 3) % 3]).outline()
            pygame.draw.lines(display, (200, 150, 150), 1, olist)

            display.blit(self.walkStop[(self.walkCount // 3) % 3], (self.pos[0], self.pos[1]))

           # display.blit(self.walkStop[0], (self.pos[0], self.pos[1]+0))
           # display.blit(self.walkStop[1], (self.pos[0], self.pos[1]-75))
            #display.blit(self.walkStop[2], (self.pos[0], self.pos[1]-150))
            #display.blit(self.walkStop[3], (self.pos[0], self.pos[1]-225))
            self.walkCount += 1


