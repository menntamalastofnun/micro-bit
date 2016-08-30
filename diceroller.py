# Add your Python code here. E.g.
from microbit import *
from random import randint

class Die:
    def __init__(self, sides):
        self.sides = sides
    
    def roll(self):
        return randint(1,self.sides)    
        
class Dices:
    def __init__(self, dices):
        self.dices = dices
        self.selected = 0
        
    def get_selected(self):
        return self.dices[self.selected].sides
    
    def get_next(self):
        self.selected = (self.selected+1)%len(self.dices)

    def get_prev(self):
        self.selected = (self.selected-1)%len(self.dices)

    def roll(self):
        return self.dices[self.selected].roll()

my_dices = Dices([Die(4),Die(6),Die(8),Die(10),Die(12),Die(20)])

while True:
    if accelerometer.was_gesture('shake'):
        display.scroll(str(my_dices.roll()))
        
    if button_a.was_pressed():
        my_dices.get_prev()
        display.scroll(str(my_dices.get_selected()))
    elif button_b.was_pressed():
        my_dices.get_next()
        display.scroll(str(my_dices.get_selected()))
    sleep(100)
