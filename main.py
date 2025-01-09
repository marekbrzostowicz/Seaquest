import pygame
from player import Player
from bubble import Bubble
from oxygen_bar import OxygenBar
from bubble_oxygen import BubbleOxygen
from heart import Heart
from text import Text
from diamond import Diamond
from enemy import Enemy
from jellyfish import Jellyfish
from enemy_2 import Enemy_2

pygame.init()
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
FPS = 30

BACKGROUND = pygame.image.load("./assets/background.png")
BACKGROUND = pygame.transform.scale(BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT))

BACKGROUND_MENU = pygame.image.load("./assets/menu_background.png")
BACKGROUND_MENU = pygame.transform.scale(BACKGROUND_MENU, (SCREEN_WIDTH, SCREEN_HEIGHT))
font = pygame.font.Font("./font/Grand9K Pixel.ttf", 70)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Seaquest")

def menu():
    clock = pygame.time.Clock()
    menu_running = True
    click = False
    while menu_running:
        screen.blit(BACKGROUND_MENU, (0, 0))
        title = font.render("SEAQUEST", True, (33, 6, 126))
        screen.blit(title, (400, 100))
        
        mx, my = pygame.mouse.get_pos()
        
        button_play = pygame.Rect(520, 320, 200, 70)
        button_quit = pygame.Rect(520, 430, 200, 70)
  
        if button_play.collidepoint((mx, my)):
            if click:
                game_loop()
        if button_quit.collidepoint((mx, my)):
            if click:
                pygame.quit()
                exit()
        
  
        
        play_text = font.render("Play", True, (33, 6, 126))
        quit_text = font.render("Quit", True, (33, 6, 126))
        screen.blit(play_text, (530, 300))
        screen.blit(quit_text, (530, 410))
        
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        
        pygame.display.update()
        clock.tick(FPS)

def game_over():
    clock = pygame.time.Clock()
    game_over_running = True
    click = False
    while game_over_running:
        screen.blit(BACKGROUND_MENU, (0, 0))
        title = font.render("GAME OVER", True, (33, 6, 126))
        screen.blit(title, (400, 100))
        
        mx, my = pygame.mouse.get_pos()
        
    
        button_play_again = pygame.Rect(520, 320, 300, 70)
        button_quit = pygame.Rect(520, 430, 200, 70)

  
        if button_play_again.collidepoint((mx, my)):
            if click:
                game_loop()
        if button_quit.collidepoint((mx, my)):
            if click:
                pygame.quit()
                exit()
        
        
        
        play_again_text = font.render("Play Again", True, (33, 6, 126))
        quit_text = font.render("Quit", True, (33, 6, 126))
        screen.blit(play_again_text, (450, 310))
        screen.blit(quit_text, (540, 410))
        
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        
        pygame.display.update()
        clock.tick(FPS)

def game_loop():
    player = Player()
    bubble = Bubble()
    oxygen_bar = OxygenBar()
    bubble_oxygen = BubbleOxygen()
    heart = Heart(player)
    text = Text()
    diamond = Diamond(text, player)
    enemy = Enemy(player, text)
    enemy_2 = Enemy_2(player, text)
    jellyfish = Jellyfish(player)

    game_is_on = True
    clock = pygame.time.Clock()

    while game_is_on:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_is_on = False

        screen.blit(BACKGROUND, (0, 0))

        player_coordinates = player.return_coordinates()

        # --------------------------------------------------- PASEK Z TLENEM
        oxygen_bar.draw_bar(screen)
        oxygen_bar.set_oxygen_bar(1, "minus")

        # --------------------------------------------------- SERCE

        heart.update_animation()
        heart.draw_heart(screen)

        # --------------------------------------------------- BABELKI

        bubble.add_bubble()
        bubble.draw_bubble(screen)
        bubble.move_bubble()

        # --------------------------------------------------- PLAYER

        player.move_player()
        player.draw_player(screen)
        player.draw(screen)
        player.draw_hp_bar(screen)

        # --------------------------------------------------- BABELKI Z TLENEM

        bubble_oxygen.add_bubble()
        bubble_oxygen.draw_bubble(screen)
        bubble_oxygen.update_animation()
        bubble_oxygen.move_bubble()

       # ------------------------------------------------------ PRZECIWNICY
        enemy.add_enemy()
        enemy.add_bullet()
        enemy.draw(screen)
        enemy.move()
        bullets_cords = player.get_list_bullet()
        enemy.remove(bullets_cords, player_coordinates)

        enemy_2.add_enemy()
        enemy_2.add_bullet()
        enemy_2.draw(screen)
        enemy_2.move()
        enemy_2.remove(bullets_cords, player_coordinates)

        # -----------------------------------------------------MEDUZA
        jellyfish.update_animation()
        jellyfish.start_point()
        jellyfish.move(screen)
        jellyfish.collision()

        # ------------------------------------------------TEKST
        text.draw_font(screen)

    
        oxygen_rectangles = bubble_oxygen.get_list_of_rectangles()
        for rect_bubble_oxygen in oxygen_rectangles:
            for rect_player in player_coordinates:
                if rect_player.colliderect(rect_bubble_oxygen):
                    oxygen_bar.set_oxygen_bar(15, "plus")
                    bubble_oxygen.remove(rect_bubble_oxygen.x - 5)
                    break

        # ---------------------------------------------DIAMENT
        diamond.check_points(screen)
        diamond.draw_diamond(screen)

        if player.health <= 0 or oxygen_bar.oxygen_bar <= 0:
            game_is_on = False

        if len(diamond.diamond_list) == 4:
            diamond.diamond_list.clear()
            text.points = 0
            diamond.i = 38
            diamond.last_point = 0
            diamond.flag = True
            text.level += 1
            enemy.bullet_cooldown -= 5
            enemy_2.bullet_cooldown -= 5

        pygame.display.update()

    game_over()

menu()