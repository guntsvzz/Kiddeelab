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


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
    screen.blit(sky_surf,(0,0))
    screen.blit(ground_surf,(0,300))
    pygame.display.update()
    clock.tick(60)