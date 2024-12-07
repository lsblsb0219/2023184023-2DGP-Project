from pico2d import *

import game_world


class Hoe:
    image = None

    def __init__(self, x, y):
        if Hoe.image == None:
            Hoe.image = load_image('resource/hoeDirt.png')
        self.x, self.y = x, y


    def draw(self):
        self.image.clip_draw(0, 50, 15, 15, self.x, self.y, 50, 50)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def get_bb(self):
        return self.x-23,self.y-23,self.x+23,self.y+23
        pass

    def handle_collision(self, group, other):
        if group == 'hoe:hoe':
            game_world.remove_object(self)


