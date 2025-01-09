
import pygame, random

class SingleEnemy(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, hp):
        super().__init__()

        self.image_left = pygame.transform.scale(pygame.image.load("./assets/enemy.png"), (110, 110))
        self.image_right = pygame.transform.flip(self.image_left, True, False)

        self.image = self.image_left

        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.collision_rect = self.rect.copy()
        self.collision_rect.inflate_ip(-60, -60)
        self.collision_rect.topleft = (x + 35, y + 30)


        self.direction = direction

        self.hp = hp
        self.bullet_cooldown = 70


    def update(self):
        if self.direction == 'left':
            self.image = self.image_left
        else:
            self.image = self.image_right



# ------------------------------------------BULLET--------------------------------------------------------------------------

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        super().__init__()
        self.image = pygame.Surface((25, 3))
        self.image.fill((255, 189, 77))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.direction = direction

# ---------------------------------------------------------------------------------------------------------------------

class Enemy(pygame.sprite.Sprite):
    def __init__(self, player, text):
        super().__init__()
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.hp_bars = pygame.sprite.Group()
        self.tick = 0
        self.tick_bullet = 0
        self.player = player
        self.text = text

        self.bullet_cooldown = 70

    def add_enemy(self):
        self.tick += 1
        if self.tick > 350:
            for i in range(100, 600, 150):
                enemy = SingleEnemy(-100, i, 'left', 80)
                self.enemies.add(enemy)

                enemy = SingleEnemy(1200, i, 'right', 80)
                self.enemies.add(enemy)

            self.tick = 0

    def add_bullet(self):

        self.tick_bullet += 1
        if self.tick_bullet > self.bullet_cooldown:
            for enemy in self.enemies:
                if enemy.direction == 'left':
                    bullet = Bullet(enemy.rect.x + 100, enemy.rect.y + 50, 'left')
                    self.bullets.add(bullet)
                else:
                    bullet = Bullet(enemy.rect.x - 10, enemy.rect.y + 50, 'right')
                    self.bullets.add(bullet)
            self.tick_bullet = 0

    def draw(self, screen):
        self.enemies.update()
        self.enemies.draw(screen)
        self.bullets.update()
        self.bullets.draw(screen)

        for enemy in self.enemies:
            pygame.draw.rect(screen, (118,255,97), (enemy.rect.x + 15, enemy.rect.y + 100, enemy.hp, 3))

        # for bullet in self.bullets:
        #     pygame.draw.rect(screen, (0,0,0), bullet.rect, )

    def move(self):
        for enemy in self.enemies:
            if enemy.direction == 'left':
                enemy.rect.x += 5
                enemy.collision_rect.x += 5
                if enemy.rect.x > 1200:
                    enemy.kill()
            else:
                enemy.rect.x -= 5
                enemy.collision_rect.x -= 5
                if enemy.rect.x < -100:
                    enemy.kill()

        for bullet in self.bullets:
            if bullet.direction == 'left':
                bullet.rect.x += 11
                if bullet.rect.x < -100:
                    bullet.kill()
            else:
                bullet.rect.x -= 11
                if bullet.rect.x > 1200:
                    bullet.kill()


    def remove(self, list_to_check, player_cords):

        for enemy in self.enemies:
            collided_enemy = []
            for sprite in list_to_check:
                if enemy.collision_rect.colliderect(sprite.rect):
                    collided_enemy.append(sprite)

            for sprite in collided_enemy:
                list_to_check.remove(sprite)
                enemy.hp -= 20
                if enemy.hp == 0:
                    self.text.add_point()
                    enemy.kill()

            for enemy in self.enemies:
                for position in player_cords:
                    if enemy.collision_rect.colliderect(position):
                        enemy.kill()
                        self.player.set_health_bar(10, "minus")
                        break

            for position in player_cords:
                for bullet in self.bullets:
                    if bullet.rect.colliderect(position):
                        self.player.set_health_bar(7, "minus")
                        bullet.kill()
                        break

    
