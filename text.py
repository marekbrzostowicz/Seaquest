import pygame

class Text:
    def __init__(self):
        self.points = 0
        self.level = 1

    def draw_font(self, screen):
        rect_surface = pygame.Surface((1200, 80), pygame.SRCALPHA)
        rect_surface.fill((22, 18, 59, 128))
        screen.blit(rect_surface, (0, 0))

        font = pygame.font.Font("./font/Grand9K Pixel.ttf", 40)
        points = font.render(str(self.points), True, (92, 233, 255))
        level = font.render("level  " + str(self.level), True, (92, 233, 255))
        screen.blit(points, (700, 10))
        screen.blit(level, (900, 10))

        pygame.draw.polygon(screen, (153, 201, 255), [(90, 20), (110, 40), (90, 60), (70, 40)],4)
        pygame.draw.polygon(screen, (153, 201, 255), [(170, 20), (190, 40), (170, 60), (150, 40)], 4)
        pygame.draw.polygon(screen, (153, 201, 255), [(250, 20), (270, 40), (250, 60), (230, 40)], 4)
        pygame.draw.polygon(screen,(153, 201, 255) , [(330, 20), (350, 40), (330, 60), (310, 40)], 4)


    def add_point(self):
        self.points += 10

    def get_points(self):
        return self.points