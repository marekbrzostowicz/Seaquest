import random
import pygame

class Heart:

    def __init__(self, player):
        self.images = [pygame.transform.scale(pygame.image.load("./assets/heart_1.png"), (170, 170)),
                       pygame.transform.scale(pygame.image.load("./assets/heart_2.png"), (170, 170))]

        self.tick = 0
        self.tick_ = 0
        self.tick__ = 0
        self.index = 0
        self.random_x = random.randint(200, 1100)
        self.random_y = random.randint(200, 500)
        self.time = 100
        self.player = player
        self.flag = True
        self.heart_sound = pygame.mixer.Sound("./sounds/serce.mp3")  

    def update_animation(self):
        self.tick += 1
        if self.tick == 20:
            self.index += 1
            if self.index == len(self.images):
                self.index = 0
            self.tick = 0

    def draw_heart(self, screen):
        self.tick_ += 1

        if self.tick_ > 700:

            if self.flag:
                screen.blit(self.images[self.index], (self.random_x, self.random_y))
                rectangle = (self.random_x + 60, self.random_y + 60, 45, 45)
            for i in range(0, self.time, 3):
                pygame.draw.rect(screen, (255,255,255), (self.random_x + 40 + i, self.random_y + 140, 3, 5))
                self.tick__ += 1
                if self.tick__ == 9:
                    self.time -= 1
                    self.tick__ = 0
                for coordinates in self.player.return_coordinates():
                    if coordinates.colliderect(rectangle):
                        self.heart_sound.play()
                        self.player.set_health_bar(None, "plus")
                        self.time = 0
                        self.flag = False
            if self.tick_ > 800:
                self.tick_ = 0
                self.random_x = random.randint(200, 1000)
                self.random_y = random.randint(200, 600)
                self.time = 100
                self.flag = True
