import pygame

pygame.mixer.init()

class SingleBullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        super().__init__()
        self.velocity = 10
        self.bullet_right = pygame.image.load("./assets/bullet.png")
        self.bullet_left = pygame.image.load("./assets/bullet_2.png")
        self.image = self.bullet_left
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.collision_rect = self.rect.copy()
        self.collision_rect.inflate_ip(-30, -40)
        self.collision_rect.topleft = (x, y + 17)

        self.direction = direction

    def update(self):
        if self.direction == 'left':
            self.image = self.bullet_left
        else:
            self.image = self.bullet_right

class Bullet(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.bullets = pygame.sprite.Group()
        self.tick = 0
        self.shoot_sound = pygame.mixer.Sound("./sounds/strzal_gracz.mp3")  

    def add_bullet(self, x, y, direction):
        self.tick += 1
        if self.tick > 7:
            bullet = SingleBullet(x, y, direction)
            self.bullets.add(bullet)
            self.shoot_sound.play() 
            self.tick = 0

    def draw(self, screen):
        self.bullets.update()
        self.bullets.draw(screen)

        for bullet in self.bullets:
            if bullet.direction == "left":
                bullet.rect.x -= 20
                bullet.collision_rect.x -= 20
                if bullet.rect.x < -10:
                    bullet.kill()
            else:
                bullet.rect.x += 20
                bullet.collision_rect.x += 20
                if bullet.rect.x > 1190:
                    bullet.kill()

        for bullet in self.bullets:
            pygame.draw.rect(screen, (255, 255, 255), bullet.collision_rect, -1)

    def get_list_bullet(self):
        return self.bullets
