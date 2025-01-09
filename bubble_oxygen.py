import pygame, random


class BubbleOxygen:
    def __init__(self):
        self.list_of_bubble_oxygen = []
        self.list_of_bubble_oxygen_rectangles = []
        self.images = [pygame.transform.scale(pygame.image.load("./assets/bubble_oxygen.png"), (80, 80)),
                    pygame.transform.scale(pygame.image.load("./assets/bubble_oxygen_2 (2).png"), (80, 80))]
        self.tick = 0
        self.tick_ = 0
        self.index = 0


    def add_bubble(self):
        self.tick += 1
        if self.tick == 400:
            x = random.randint(100,1100)
            self.list_of_bubble_oxygen.append([x, 800])
            rectangle = pygame.Rect(x + 5, 810, 55, 55)
            self.list_of_bubble_oxygen_rectangles.append(rectangle)
            self.tick = 0

    def update_animation(self):
        self.tick_ += 1
        if self.tick_ == 7:
            self.index += 1
            if self.index == len(self.images):
                self.index = 0
            self.tick_ = 0

    def draw_bubble(self, screen):
        for coordinates in self.list_of_bubble_oxygen:
            screen.blit(self.images[self.index], coordinates)
        for rect in self.list_of_bubble_oxygen_rectangles:
            pygame.draw.rect(screen, (0,0,0), rect, -1)

    def move_bubble(self):
        for rect in self.list_of_bubble_oxygen_rectangles:
             rect[1] -= 8
             if rect[1] < -50:
                 self.list_of_bubble_oxygen_rectangles.remove(rect)

        for bubble in self.list_of_bubble_oxygen:
            bubble[1] -= 8
            if bubble[1] < -50:
                self.list_of_bubble_oxygen.remove(bubble)

    def get_list_of_rectangles(self):
        return self.list_of_bubble_oxygen_rectangles

    def remove(self, cor_1):
        for bubble in self.list_of_bubble_oxygen:
            if bubble[0] == cor_1:
                self.list_of_bubble_oxygen.remove(bubble)





