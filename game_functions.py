import time
import pygame


def check_events(snake, game_settings, again_rect, fruit):
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    quit()

            if game_settings.game_over:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    check_play_again(pygame.mouse.get_pos(), again_rect, game_settings, snake, fruit)
            elif event.type == pygame.KEYDOWN:
                    check_keydown_events(snake, event.key)
                

def check_keydown_events(snake, event_key):
    if event_key == pygame.K_UP:
        snake.change_to = 'UP'
    if event_key == pygame.K_DOWN:
        snake.change_to = 'DOWN'
    if event_key == pygame.K_LEFT:
        snake.change_to = 'LEFT'
    if event_key == pygame.K_RIGHT:
        snake.change_to = 'RIGHT'

def check_play_again(pos, again_rect, game_settings, snake, fruit):
    if again_rect.collidepoint(pos):
        game_settings.game_over = False
        snake.new_snake() 
        fruit.spawn = True
        fruit.create_fruit(game_settings)



def eat_if_can(snake, fruit, game_settings):
    snake.body.insert(0, list(snake.position))
    if snake.position[0] == fruit.position[0] and snake.position[1] == fruit.position[1]:
        #eatting_sound.play()
        snake.score += 10
        fruit.spawn = False
    else:
        snake.body.pop()
    
    # if ate, create new fruit
    if not fruit.spawn:
        fruit.create_fruit(game_settings)
    fruit.spawn = True


def check_game_over(snake, game_settings, screen):
    if snake.position[0] < 0 or snake.position[0] > game_settings.screen_width-20:
        draw_game_over(snake, game_settings, screen)
    if snake.position[1] < 0 or snake.position[1] > game_settings.screen_height-20:
        draw_game_over(snake, game_settings, screen)

    # Touching the snake body
    for block in snake.body[1:]:
        if snake.position[0] == block[0] and snake.position[1] == block[1]:
            draw_game_over(snake, game_settings, screen)


def draw_game_over(snake, game_settings, screen):

    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render('Your Score is : ' + str(snake.score), True, (255, 255, 255))
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (game_settings.screen_width/2, game_settings.screen_height/4)
    screen.blit(game_over_surface, game_over_rect)
    
    game_settings.game_over = True
    
    pygame.display.flip()
    #time.sleep(2)
    #pygame.quit()
    #quit()


def show_score(choice, color, font, size, snake, screen):
  score_font = pygame.font.SysFont(font, size)
  score_surface = score_font.render('Score : ' + str(snake.score), True, color)
  score_rect = score_surface.get_rect()
  
  screen.blit(score_surface, score_rect)

def play_again(game_settings, screen, again_rect):
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    font = pygame.font.SysFont(None, 40)
    again_text = 'Play Again :)'
    again_img = font.render(again_text, True, BLUE)
    pygame.draw.rect(screen, GREEN, again_rect)
    screen.blit(again_img, (game_settings.screen_width // 2 - 80, game_settings.screen_height // 2 + 10))
