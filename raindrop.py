# Add your Python code here. E.g.
from microbit import *
import random

class Bucket:
    def __init__(self):
        self.x = 2
        self.y = 4
        self.value = 9
        self.drops = 0
    
    def move_right(self):
        if self.x < 4:
            self.x += 1
    
    def move_left(self):
        if self.x > 0:
            self.x -= 1

class Raindrop:
    def __init__(self):
        self.x = random.randint(0,4)
        self.y = 0
        self.value = 9
    
    def move_down(self):
        if self.y < 4:
            self.y += 1

bucket = Bucket()
raindrops = []

def update_raindrops():
    for drop in raindrops:
        drop.move_down()

def score_raindrop():
    for drop in raindrops:
        if drop.x == bucket.x and drop.y == bucket.y:
            bucket.drops += 1
            raindrops.remove(drop)

def delete_raindrops():
    for drop in raindrops:
        if drop.y == 4:
            bucket.value -= 1
    raindrops[:] = [drop for drop in raindrops if drop.y < 4]

def create_raindrop():
    if random.randint(0,2) == 0:
        raindrops.append(Raindrop())
    if len(raindrops) == 0:
        raindrops.append(Raindrop())


def draw_scene():
    display.set_pixel(bucket.x, bucket.y, bucket.value)
    for drop in raindrops:
        display.set_pixel(drop.x, drop.y, drop.value)

while bucket.value > 0:
    if button_a.was_pressed():
        bucket.move_left()
    elif button_b.was_pressed():
        bucket.move_right()
    
    update_raindrops()
    score_raindrop()
    create_raindrop()
    delete_raindrops()
    draw_scene()
    
    sleep(1000)
    display.clear()

while True:
    display.scroll('Stig: '+str(bucket.drops))
