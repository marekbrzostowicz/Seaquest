import pygame
class OxygenBar:
    def __init__(self):
        self.x = 300
        self.y = 730
        self.oxygen_bar = 600
        self.tick = 0
    def set_oxygen_bar(self, wartosc, znak):

        if znak == "minus":
            self.tick += 1
            if self.tick == 4:
                self.oxygen_bar -= wartosc
                self.tick = 0
        else:
            self.oxygen_bar = 600

    def draw_bar(self, screen):
        pygame.draw.rect(screen, (209,227,255), (290,720, 620, 35), 3)
        for i in range(0,self.oxygen_bar, 10):
            pygame.draw.rect(screen,(144, 186, 252), (self.x + i, self.y, 10, 15), 0)

    def get_oxygen_bar(self):
        return self.oxygen_bar



