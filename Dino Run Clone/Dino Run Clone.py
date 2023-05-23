import os
import pygame
import random

pygame.init()

class ImgLoad:
    def load_image(file_name):
        return pygame.image.load(os.path.join("images", file_name))


class Settings:
    SCREEN_HEIGHT = 600
    SCREEN_WIDTH = 1100
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    JUMPING = ImgLoad.load_image("DinoJump.png")
    CLOUD = ImgLoad.load_image("Cloud.png")
    BG = ImgLoad.load_image("Track.png")

    RUNNING = [
        ImgLoad.load_image("DinoRun1.png"),
        ImgLoad.load_image("DinoRun2.png"),
    ]

    DUCKING = [
        ImgLoad.load_image("DinoDuck1.png"),
        ImgLoad.load_image("DinoDuck2.png"),
    ]

    SMALL_CACTUS = [
        ImgLoad.load_image("SmallCactus1.png"),
        ImgLoad.load_image("SmallCactus2.png"),
        ImgLoad.load_image("SmallCactus3.png"),
    ]

    LARGE_CACTUS = [
        ImgLoad.load_image("LargeCactus1.png"),
        ImgLoad.load_image("LargeCactus2.png"),
        ImgLoad.load_image("LargeCactus3.png"),
    ]

    BIRD = [
        ImgLoad.load_image("Bird1.png"),
        ImgLoad.load_image("Bird2.png"),
    ]

class DinoSettings:
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_VEL = 8.5


class Dino:
    def __init__(self):
        self.duck_img = Settings.DUCKING
        self.run_img = Settings.RUNNING
        self.jump_img = Settings.JUMPING

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.step_index = 0
        self.jump_vel = DinoSettings.JUMP_VEL
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = DinoSettings.X_POS
        self.dino_rect.y = DinoSettings.Y_POS

    def update(self, usr_input):
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()

        if self.step_index >= 10:
            self.step_index = 0

        if usr_input[pygame.K_UP] and not self.dino_jump:
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True
        elif usr_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
        elif not (self.dino_jump or usr_input[pygame.K_DOWN]):
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False

    def duck(self):
        self.image = self.duck_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = DinoSettings.X_POS
        self.dino_rect.y = DinoSettings.Y_POS_DUCK
        self.step_index += 1

    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = DinoSettings.X_POS
        self.dino_rect.y = DinoSettings.Y_POS
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel <- DinoSettings.JUMP_VEL:
            self.dino_jump = False
            self.jump_vel = DinoSettings.JUMP_VEL

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))


class Cloud:
    def __init__(self):
        self.x = Settings.SCREEN_WIDTH + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image = Settings.CLOUD
        self.width = self.image.get_width()

    def update(self):
        self.x -= Game.game_speed
        if self.x < -self.width:
            self.x = Settings.SCREEN_WIDTH + random.randint(2500, 3000)
            self.y = random.randint(50, 100)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))


class Obstacle:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = Settings.SCREEN_WIDTH

    def update(self):
        self.rect.x -= Game.game_speed
        if self.rect.x < -self.rect.width:
            Game.obstacles.pop()

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)


class SmallCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 325


class LargeCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 300


class Bird(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 250
        self.index = 0

    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index // 5], self.rect)
        self.index += 1

class Game:
    run = True
    clock = pygame.time.Clock()
    player = Dino()
    cloud = Cloud()
    game_speed = 20
    x_pos_bg = 0
    y_pos_bg = 380
    points = 0
    font = pygame.font.Font("freesansbold.ttf", 20)
    obstacles = []
    death_count = 0   


class Score:
    def draw():
        Game.points += 1
        if Game.points % 100 == 0:
            Game.game_speed += 1
        text = Game.font.render("Points: " + str(Game.points), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (Settings.SCREEN_WIDTH - 60, 40)
        Settings.SCREEN.blit(text, textRect)

class Background:
    def draw():
        image_width = Settings.BG.get_width()
        Settings.SCREEN.blit(Settings.BG, (Game.x_pos_bg, Game.y_pos_bg))
        Settings.SCREEN.blit(Settings.BG, (image_width + Game.x_pos_bg, Game.y_pos_bg))
        if Game.x_pos_bg <= -image_width:
            Settings.SCREEN.blit(Settings.BG, (image_width + Game.x_pos_bg, Game.y_pos_bg))
            Game.x_pos_bg = 0
        Game.x_pos_bg -= Game.game_speed


def main():
    while Game.run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Game.run = False

        Settings.SCREEN.fill((255, 255, 255))
        usr_input = pygame.key.get_pressed()

        Background()

        Game.player.draw(Settings.SCREEN)
        Game.player.update(usr_input)

        if len(Game.obstacles) == 0:
            if random.randint(0, 2) == 0:
                Game.obstacles.append(SmallCactus(Settings.SMALL_CACTUS))
            elif random.randint(0, 2) == 1:
                Game.obstacles.append(LargeCactus(Settings.LARGE_CACTUS))
            elif random.randint(0, 2) == 2:
                Game.obstacles.append(Bird(Settings.BIRD))

        for obstacle in Game.obstacles:
            obstacle.draw(Settings.SCREEN)
            obstacle.update()
            if Game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(2000)
                Game.death_count += 1
                menu(Game.death_count)

        Background.draw()

        Game.cloud.draw(Settings.SCREEN)
        Game.cloud

        Score.draw()

        Game.clock.tick(30)
        pygame.display.update()

def menu(death_count):
    while Game.run:
        pygame.display.set_caption("Dino Run Clone")
        Settings.SCREEN.fill((255, 255, 255))
        font = pygame.font.Font('freesansbold.ttf', 30)

        if death_count == 0:
            text = font.render("Press any Key to Start accept ESC", True, (0, 0, 0))
        elif death_count > 0:
            text = font.render("Game Over! Exit with ESC or press 'X' ", True, (0, 0, 0))
            score = font.render("Your Score: " + str(Game.points), True, (0, 0, 0))
            scoreRect = score.get_rect()
            scoreRect.center = (Settings.SCREEN_WIDTH // 2, Settings.SCREEN_HEIGHT // 2 + 50)
            Settings.SCREEN.blit(score, scoreRect)
        textRect = text.get_rect()
        textRect.center = (Settings.SCREEN_WIDTH // 2, Settings.SCREEN_HEIGHT // 2)
        Settings.SCREEN.blit(text, textRect)
        Settings.SCREEN.blit(Settings.RUNNING[0], (Settings.SCREEN_WIDTH // 2 - 20, Settings.SCREEN_HEIGHT // 2 - 140))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Game.run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Game.run = False                  
            if event.type == pygame.KEYDOWN:
                main()

menu(death_count=0)