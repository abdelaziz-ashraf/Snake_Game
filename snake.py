import pygame

class Snake():

    def __init__(self):
        self.new_snake()

    def new_snake(self):
        self.position = [100, 40]
        self.SNAKE_SPEED = 15
        self.body = [ [100, 40],
                            [80, 40],
                            [60, 40],
                            [40, 40] ]
        self.direction = 'RIGHT'
        self.change_to = self.direction
        self.score = 0
        self.head_directions = self.load_head_images()
        self.body_directions = self.load_body_images()




    def load_head_images(self):
        head_up = pygame.image.load("images\\head_up.png")
        head_up = pygame.transform.scale(head_up, (20, 20))

        head_right = pygame.image.load("images\\head_right.png")
        head_right = pygame.transform.scale(head_right, (20, 20))

        head_down = pygame.image.load("images\\head_down.png")
        head_down = pygame.transform.scale(head_down, (20, 20))

        head_left = pygame.image.load("images\\head_left.png")
        head_left = pygame.transform.scale(head_left, (20, 20))

        return [head_up, head_right, head_down, head_left]   

    def load_body_images(self):
        body_up = pygame.image.load("images\\body_up.png")
        body_up = pygame.transform.scale(body_up, (20, 20))

        body_down = pygame.image.load("images\\body_down.png")
        body_down = pygame.transform.scale(body_down, (20, 20))

        body_left = pygame.image.load("images\\body_left.png")
        body_left = pygame.transform.scale(body_left, (20, 20))

        body_right = pygame.image.load("images\\body_right.png")
        body_right = pygame.transform.scale(body_right, (20, 20))

        return [body_up, body_right, body_down, body_left]

    def draw_sanke(self, screen):
        self.draw_snake_head(screen)
        self.draw_snake_body(screen)

    def draw_snake_head(self, screen):
        if self.direction == 'UP':
            screen.blit(self.head_directions[0], (self.body[0][0], self.body[0][1]))
        if self.direction == 'RIGHT':
            screen.blit(self.head_directions[1], (self.body[0][0], self.body[0][1]))
        if self.direction == 'DOWN':
            screen.blit(self.head_directions[2], (self.body[0][0], self.body[0][1]))
        if self.direction == 'LEFT':
            screen.blit(self.head_directions[3], (self.body[0][0], self.body[0][1]))
        
    def draw_snake_body(self, screen):
        for pos in self.body[1:]:
            if self.direction == 'UP':
                screen.blit(self.body_directions[0], (pos[0], pos[1]))
            if self.direction == 'RIGHT':
                screen.blit(self.body_directions[1], (pos[0], pos[1]))
            if self.direction == 'DOWN':
                screen.blit(self.body_directions[2], (pos[0], pos[1]))
            if self.direction == 'LEFT':
                screen.blit(self.body_directions[3], (pos[0], pos[1]))

    def change_direction(self):
        if self.change_to == 'UP' and self.direction != 'DOWN':
            self.direction = 'UP'
        if self.change_to == 'DOWN' and self.direction != 'UP':
            self.direction = 'DOWN'
        if self.change_to == 'LEFT' and self.direction != 'RIGHT':
            self.direction = 'LEFT'
        if self.change_to == 'RIGHT' and self.direction != 'LEFT':
            self.direction = 'RIGHT'   

    def move(self):
        if self.direction == 'UP':
            self.position[1] -= 20
        if self.direction == 'DOWN':
            self.position[1] += 20
        if self.direction == 'LEFT':
            self.position[0] -= 20
        if self.direction == 'RIGHT':
            self.position[0] += 20

    

