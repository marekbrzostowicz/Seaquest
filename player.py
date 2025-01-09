import pygame
import random
from bullet import Bullet

class Player(Bullet):

    def __init__(self):
        super().__init__()
        self.x = 500
        self.y = 300
        self.vel = 8
        self.image_left = [pygame.image.load("./assets/lewo1.png"),
                           pygame.image.load("./assets/lewo2.png"),
                           pygame.image.load("./assets/lewo3.png")]

        self.image_right = [pygame.image.load("./assets/prawo1.png"),
                           pygame.image.load("./assets/prawo2.png"),
                           pygame.image.load("./assets/prawo3.png")]

        self.current_image = pygame.image.load("./assets/prawo3.png") 
        self.image_tick = 0
        self.image_index = 0
        self.direction = ""
        self.list_of_player_coordinates = []
        self.health = 100
        self.color = [(20, 217, 131), (252, 202, 76), (254, 69, 24)]
        self.i = 0
        self.tick_push = 0
        self.pushing = False


    def draw_player(self, screen):
            screen.blit(self.current_image, (self.x,self.y))
            if self.direction == "right":
                rect_player = pygame.Rect(self.x + 75, self.y + 55, 50, 40)
                #pygame.draw.rect(screen, (0, 0, 0), rect_player, 100, 2)

            else:
                rect_player = pygame.Rect(self.x + 35, self.y + 55, 50, 40)
                #pygame.draw.rect(screen, (0,0,0), rect_player, 100, 2)
            self.list_of_player_coordinates.append(rect_player)
            #print(self.list_of_player_coordinates)

            if len(self.list_of_player_coordinates) >= 2:
                del self.list_of_player_coordinates[0]

    def update_animation(self, array):
        self.image_tick += 1

        if self.image_tick == 3:
            self.current_image = array[self.image_index]
            self.image_index += 1
            if self.image_index == len(array):
                self.image_index = 0
            self.image_tick = 0

    def move_player(self):
        keys = pygame.key.get_pressed()
        moving = False
        if keys[pygame.K_LEFT] and self.x  > -25:
            moving = True
            self.x -= self.vel
            self.direction = "left"

        if keys[pygame.K_RIGHT] and self.x < 1065:
            moving = True
            self.x += self.vel
            self.direction = "right"

        if keys[pygame.K_UP] and self.y > 29:
            self.y -= self.vel
            moving = True

        if keys[pygame.K_DOWN] and self.y < 700:
            self.y += self.vel
            moving = True

        if keys[pygame.K_SPACE]:
            if self.direction == "right":
                self.add_bullet(self.x + 120, self.y + 57.6, self.direction)

            if self.direction == "left":
                self.add_bullet(self.x + 7, self.y + 57.6, self.direction)

        if moving:
            if self.direction == "right":
                self.update_animation(self.image_right)
            elif self.direction == "left":
                self.update_animation(self.image_left)
        else:
            if self.direction == "right":
                self.update_animation(self.image_right)
            elif self.direction == "left":
                self.update_animation(self.image_left)

    def return_coordinates(self):
        return self.list_of_player_coordinates

    def draw_hp_bar(self, screen):
        border = pygame.Rect(self.x + 35, self.y + 110, 110, 12)
        pygame.draw.rect(screen, (168, 255, 213), border, 2)

        for i in range(0, self.health, 5):
            pygame.draw.rect(screen, self.color[self.i], (self.x + 40 + i, self.y + 114.5, 5, 4),0)

    def set_health_bar(self, wartosc, znak):
        if znak == "minus":
            self.health -= wartosc
        else:
            self.health = 100
            print(self.health)
        if self.health > 65:
            self.i = 0
        elif 35 < self.health < 65:
            self.i = 1
        elif self.health < 35:
            self.i = 2

    def return_health(self):
        return self.health

    def push(self, znak):
        if znak == "left":
            self.x -= 70 
            self.y -= 70         
        else:
            self.x += 70 
            self.y -= 70
