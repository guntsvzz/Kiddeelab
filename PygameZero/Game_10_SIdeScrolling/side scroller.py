# Improvements
# 1) Remove the laser when it leaves the screen
# 2) Remove the meteor when it leaves the screen
# 3) Game over if player touches meteor
# 4) Slow down the laser (maybe 5 lasers per second)

import pgzrun
import random

WIDTH = 800
HEIGHT = 600

ship = Actor('playership1_blue')
ship.x = 400
ship.y = 300
ship.angle = -90

lasers = []
meteors = []
meteor_timer = 0

def update(): # runs 60 times per second
    global meteor_timer
    
    if keyboard.up:
        ship.y -= 5

    if keyboard.down:
        ship.y += 5

    if keyboard.left:
        ship.x -= 5

    if keyboard.right:
        ship.x += 5

    if keyboard.space:
        laser = Actor('laserblue04')
        laser.x = ship.x
        laser.y = ship.y
        lasers.append(laser)

    for laser in lasers:
        laser.x += 15

    meteor_timer += 1
    if meteor_timer == 30:
        meteor = Actor('meteorgrey_big3')
        meteor.x = 850
        meteor.y = random.randint(50, 550)
        meteors.append(meteor)
        meteor_timer = 0

    for meteor in meteors:
        meteor.x -= 3

    for laser in lasers:
        for meteor in meteors:
            if laser.colliderect(meteor):
                meteors.remove(meteor)
                lasers.remove(laser)

def draw():
    screen.fill((80,0,70))
    ship.draw()
    for laser in lasers:
        laser.draw()
    for meteor in meteors:
        meteor.draw()

pgzrun.go() # Must be last line
