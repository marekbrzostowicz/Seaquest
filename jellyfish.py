import pygame, random

class Jellyfish:

    def __init__(self, player):

        self.images = [pygame.transform.scale(pygame.image.load("./assets/jellyfish_2.png"), (170, 170)),
                      pygame.transform.scale(pygame.image.load("./assets/jellyfish.png"), (170, 170)),
                      pygame.transform.scale(pygame.image.load("./assets/jellyfish_3.png"), (170, 170))]
        self.tick = 0
        self.player = player
        self.list_of_jellyfish = []
        self.list_of_hitbox = []
        self.flag = True
        self.flag_2 = True
        self.index = 0
        self.tick_ = 0
        self.speed = 15

    def update_animation(self):
        self.tick_ += 1
        if self.tick_ > 5:
            self.index += 1
            if self.index == len(self.images):
                self.index = 0
            self.tick_ = 0


    def start_point(self):
        self.tick += 1
        if self.tick > 200:
            for coordinates in self.player.return_coordinates():
                self.list_of_jellyfish.append([coordinates[0] - 70, 800])
                rect = pygame.Rect(coordinates[0] + 40 - 70 , 800 + 20, 30, 30)
                rect_2 = pygame.Rect(coordinates[0] + 90 - 70, 800 + 20, 30, 30)
                self.list_of_hitbox.append([rect, rect_2])
                if len(self.list_of_jellyfish) > 1:
                    break
                print(self.list_of_jellyfish)
            self.tick = 0

    def move(self, screen):
        for jellyfish in self.list_of_jellyfish:
            screen.blit(self.images[self.index], jellyfish)
            jellyfish[1] -= 13
        for rect in self.list_of_hitbox:
            if len(self.list_of_hitbox) != 0:
            #pygame.draw.rect(screen, (0,0,0), rect[0], 4)
            #pygame.draw.rect(screen, (0, 0, 0), rect[1], 4)
                rect[0][1] -= 13
                rect[1][1] -= 13

            if rect[0][1] < 100:
                del self.list_of_hitbox[0]

    def collision(self):

            for coordinates in self.player.return_coordinates():
                for rect in self.list_of_hitbox:
                    if coordinates.colliderect(rect[0]):
                        self.player.push("left")
                        del self.list_of_hitbox[-1]
                        print("push left")

                    elif coordinates.colliderect(rect[1]):
                        self.player.push("right")
                        del self.list_of_hitbox[-1]
                        print("push right")
