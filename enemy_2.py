import pygame, random

class SingleEnemy(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, hp):
        super().__init__()
       
        self.image_left = pygame.transform.scale(pygame.image.load("./assets/enemy_2.png"), (100, 90))
        self.image_right = pygame.transform.flip(self.image_left, True, False)
        
        self.image = self.image_left

        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.collision_rect = self.rect.copy()
        self.collision_rect.inflate_ip(-60, -60)
        self.collision_rect.topleft = (x + 35, y + 30)

        self.direction = direction

        self.hp = hp
    
    def update(self):
        if self.direction == 'left':
            self.image = self.image_left
        else:
            self.image = self.image_right

# ------------------------------------------DOUBLE BULLET--------------------------------------------------------------------------

class DoubleBullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, y_direction):
        super().__init__()
        self.image = pygame.Surface((25, 3))
        self.image.fill((252, 111, 139))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.direction = direction
        self.y_direction = y_direction

    def update(self):
        if self.direction == 'left':
            self.rect.x -= 6
        else:
            self.rect.x += 6

        self.rect.y += self.y_direction

# ---------------------------------------------------------------------------------------------------------------------

class Enemy_2(pygame.sprite.Sprite):
    def __init__(self, player, text):
        super().__init__()
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.hp_bars = pygame.sprite.Group()
        self.tick = 0
        self.tick_bullet = 0
        self.player = player
        self.text = text
        self.bullet_cooldown = 60

    def add_enemy(self):
        self.tick += 1
        if self.tick > 80:
            random_number = random.randint(0, 1)
            if random_number == 0:
                enemy = SingleEnemy(-100, random.randint(200, 600), 'left', 80)
                self.enemies.add(enemy)
            else:
                enemy = SingleEnemy(1200, random.randint(200, 600), 'right', 80)
                self.enemies.add(enemy)
            self.tick = 0

    def add_bullet(self):
        self.tick_bullet += 1
        if self.tick_bullet > self.bullet_cooldown:
            for enemy in self.enemies:
                if enemy.direction == 'left':
                    bullet1 = DoubleBullet(enemy.rect.x + 100, enemy.rect.y + 50, 'right', -1)
                    bullet2 = DoubleBullet(enemy.rect.x + 100, enemy.rect.y + 50, 'right', 1)
                    self.bullets.add(bullet1, bullet2)
                else:
                    bullet1 = DoubleBullet(enemy.rect.x - 10, enemy.rect.y + 50, 'left', -1)
                    bullet2 = DoubleBullet(enemy.rect.x - 10, enemy.rect.y + 50, 'left', 1)
                    self.bullets.add(bullet1, bullet2)
            self.tick_bullet = 0

    def draw(self, screen):
        self.enemies.update()
        self.enemies.draw(screen)
        self.bullets.update()
        self.bullets.draw(screen)

        for enemy in self.enemies:
            # Pasek zdrowia
            hp_bar_width = enemy.hp
            pygame.draw.rect(screen, (0, 255, 0), (enemy.rect.x + 15, enemy.rect.y + 100, hp_bar_width, 3)) 

    def move(self):
        for enemy in self.enemies:
            if enemy.direction == 'left':
                enemy.rect.x += 6
                enemy.collision_rect.x += 6
                if enemy.rect.x > 1200:
                    enemy.kill()
            else:
                enemy.rect.x -= 6
                enemy.collision_rect.x -= 6
                if enemy.rect.x < -100:
                    enemy.kill()

        for bullet in self.bullets:
            bullet.update()

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
