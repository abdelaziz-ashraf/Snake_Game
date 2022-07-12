import pygame
import random

class Fruit():
    def __init__(self, game_settings):
        self.spawn = True
        self.position = []
        self.load_fruit_image()
        self.create_fruit(game_settings)

    def load_fruit_image(self):
        self.image = pygame.image.load("images\\fruit.png")
        self.image = pygame.transform.scale(self.image, (20, 20))

    def create_fruit(self, game_settings):
        x = game_settings.screen_width
        y = game_settings.screen_height
        self.position = [random.randrange(1, (x//20)) * 20,
                                random.randrange(1, (y//20)) * 20]
