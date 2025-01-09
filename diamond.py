import random
import pygame

class Diamond:

    def __init__(self, text, player):
        self.image = pygame.transform.scale(pygame.image.load("./assets/diamond.png"), (110, 110))
        self.text = text
        self.random_x = random.randint(100, 700)
        self.random_y = random.randint(200, 500)
        self.player = player
        self.flag = True
        self.diamond_list = []
        self.collected = True
        self.i = 38
        self.last_point = 0

    def check_points(self, screen):

        if (self.text.get_points() % 20 == 0) and (self.text.get_points() != 0):
            if self.text.get_points() != self.last_point:
                self.flag = False
                self.last_point += 20

        if not self.flag and self.collected:
            screen.blit(self.image, (self.random_x, self.random_y))
            rect = pygame.Rect(self.random_x + 30, self.random_y + 30, 50, 50)
            #pygame.draw.rect(screen, (0,0,0), rect, 2)
            for coordinates in self.player.return_coordinates():
                if rect.colliderect(coordinates): 

                    self.diamond_list.append((self.i, -12))
                    print(self.diamond_list)
                    self.i += 80
                    self.flag = True
                    self.random_x = random.randint(100, 700)
                    self.random_y = random.randint(200, 600)
                    break
                self.collected = True

    def draw_diamond(self, screen):
        for i in range(len(self.diamond_list)):
            screen.blit(self.image, self.diamond_list[i])

