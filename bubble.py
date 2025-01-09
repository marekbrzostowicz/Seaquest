import pygame.image
import random

class Bubble:
    def __init__(self):
        self.image = pygame.image.load("./assets/bubble.png")
        self.bubble_image = pygame.transform.scale(self.image, (65,60))
        self.list_of_bubbles = []

    def add_bubble(self):
            random_number = random.randint(0,30)
            if random_number == 1:
                x = random.randint(0,1200)
                self.list_of_bubbles.append([x, 800])

    def draw_bubble(self, screen):
        for coordinates in self.list_of_bubbles:
            screen.blit(self.bubble_image, coordinates)

    def move_bubble(self):
        for bubble in self.list_of_bubbles:
            random_number = random.randint(1,4)
            if random_number == 1:
                bubble[0] -= 0.5
            elif random_number == 2:
                bubble[0] += 0.5
            elif random_number == 2:
                bubble[1] -= 2
            elif random_number == 3:
                bubble[1] -= 4
