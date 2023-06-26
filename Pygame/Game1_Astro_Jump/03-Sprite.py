import pygame
import sys
import random

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Astro Jumper') #Title
clock = pygame.time.Clock()
###Setting image
sky_surf = pygame.image.load('graphics/sky.png')
ground_surf = pygame.image.load('graphics/ground.png')
###Setting Font
loaded_font = pygame.font.Font('font/Pixeltype.ttf', 50)
###Setting music
bg_music = pygame.mixer.Sound('audio/music.wav') #not mp3
bg_music.set_volume(0.07) #1
bg_music.play(loops = -1) #-1 loop


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('graphics/Player/Walking1.png').convert_alpha()
        self.rect  = self.image.get_rect(midbottom = (80,300))

        self.gravity = 0
    
    def jump(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20

    def accelator(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def movement(self):
        pass

    def update(self):
        self.accelator()
        self.jump()

class Enemy():
    def __init__(self):
        super().__init__()

    def move(self):
        pass

#Groups
player = pygame.sprite.GroupSingle()
player.add(Player())

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surf,(0,0))
    screen.blit(ground_surf,(0,300))

    player.draw(screen)
    player.update()

    pygame.display.update()
    clock.tick(60)