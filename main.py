import pygame

from fruit import Fruit
import game_functions as gf

from settings import Settings
from snake import Snake


def run_game():
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Snake")

    snake = Snake()
    fruit = Fruit(game_settings)

    fps = pygame.time.Clock()

    again_rect =  pygame.Rect((game_settings.screen_width // 2 - 80, game_settings.screen_height // 2), (180, 50))

    while True:
        gf.check_events(snake, game_settings, again_rect, fruit)

        if game_settings.game_over:
            gf.draw_game_over(snake, game_settings, screen)
            gf.play_again(game_settings, screen, again_rect) 
        else:
            snake.change_direction()
            snake.move()
            gf.eat_if_can(snake, fruit, game_settings)
            screen.fill(game_settings.bg_color)
            snake.draw_sanke(screen)
            screen.blit(fruit.image, (fruit.position[0], fruit.position[1]))
            gf.check_game_over(snake, game_settings, screen)

            gf.show_score(1, (255, 255, 255), 'times new roman', 20, snake, screen)
            pygame.display.update()
            fps.tick(snake.SNAKE_SPEED)




run_game()


