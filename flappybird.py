import random

import gamebox
import pygame

camera = gamebox.Camera(800, 600)


bird = gamebox.from_image(50, 100, "yellowbird-upflap.png")
back = gamebox.from_image(400, 200, "background-day.png")
back.scale_by(3)

topwalls = [
    gamebox.from_color(800, camera.top, 'green', 30, 300),
    gamebox.from_color(1000, camera.top, 'green', 30, 500),
    gamebox.from_color(1200, camera.top, 'green', 30, 400),
    gamebox.from_color(1400, camera.top, 'green', 30, 400),
    #gamebox.from_color(1600, camera.top, 'green', 30, 400),
    #gamebox.from_color(1800, camera.top, 'green', 30, 400)
]
bottomwalls = [
    gamebox.from_color(800, camera.bottom, 'green', 30, 500),
    gamebox.from_color(1000, camera.bottom, 'green', 30, 300),
    gamebox.from_color(1200, camera.bottom, 'green', 30, 400),
    gamebox.from_color(1400, camera.bottom, 'green', 30, 400),
    #gamebox.from_color(1600, camera.bottom, 'green', 30, 400),
    #gamebox.from_color(1800, camera.bottom, 'green', 30, 400)
]
counter = 0
game_on = False
score = 0
ticks = 0
bird.timer = 0
#starttext = gamebox.from_text(camera.x, camera.y, "Press SPACE to Start and Flap", "Arial", 20, 'black')


ground = gamebox.from_color(camera.x / 2, camera.bottom, 'brown', 1500, 50)

def tick(keys):
    global game_on
    global ticks
    global counter
    global score
    global starttext
    score += 1
    counter = score//ticks_per_second


    if pygame.K_SPACE in keys:
        game_on = True
        #camera.draw(starttext)

    camera.clear("cyan")
    camera.draw(back)
    # if bird.touches(ground):
    #     gamebox.pause()
    #     bird.speedy = 0
    #     over = gamebox.from_text(camera.left + 400, 300, "You Lost! Score: " + str(counter), "Arial", 50, 'black')
    #     camera.draw(over)


    if pygame.K_SPACE in keys and bird.timer < 30:
        # bird.y = 10
        bird.speedy = -8
        bird.timer = 0
        keys.clear()
    bird.timer += 1
    bird.speedy += 1
    if game_on == True:
        bird.move_speed()

        ticks += 1
        if ticks % 17 == 0 and ticks >= 100:
            randomnum = random.randrange(300)
            newwalltop =  gamebox.from_color(camera.x + 500, camera.top, 'green', 30, randomnum)
            newwallbottom = gamebox.from_color(camera.x + 500, camera.bottom, 'green', 30, 800 - randomnum)

            topwalls.append(newwalltop)
            bottomwalls.append(newwallbottom)

        if ticks < 100:
            if ticks % 80 == 0:
                randomnum = random.randrange(300)
                newwalltop = gamebox.from_color(camera.x + 500, camera.top, 'green', 30, randomnum)
                newwallbottom = gamebox.from_color(camera.x + 500, camera.bottom, 'green', 30, 800 - randomnum)

                topwalls.append(newwalltop)
                bottomwalls.append(newwallbottom)

        for wall in topwalls:
            camera.draw(wall)
        for wall in bottomwalls:
            camera.draw(wall)

        if bird.touches(ground):
            gamebox.pause()
            bird.speedy = 0
            over = gamebox.from_text(camera.left + 400, 300, "You Lost! Score: " + str(counter), "Arial", 50, 'black')
            camera.draw(over)

        for wall in topwalls:
            if bird.touches(wall):
                bird.move_to_stop_overlapping(wall)
                gamebox.pause()
                bird.speedx = 0
                text = gamebox.from_text(camera.x, camera.y, "You Lost! Score: " + str(counter), "Arial", 50, 'black')
                camera.draw(text)

            wall.x -= 10

        for wall in bottomwalls:
            if bird.touches(wall):
                bird.move_to_stop_overlapping(wall)
                gamebox.pause()
                bird.speedx = 0
                text = gamebox.from_text(camera.x, camera.y, "You Lost! Score: " + str(counter), "Arial", 50, 'black')
                camera.draw(text)

            wall.x -= 10
    camera.draw(ground)
    camera.draw(bird)
    camera.display()

ticks_per_second = 30

gamebox.timer_loop(ticks_per_second, tick)
