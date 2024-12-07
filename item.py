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
        if group == 'hoe:water':
            game_world.remove_object(self)


class Water:
    image = None

    def __init__(self, x, y):
        if Water.image == None:
            Water.image = load_image('resource/hoeDirtDark.png')
        self.x, self.y = x, y


    def draw(self):
        hoe_exists = any(isinstance(obj, Hoe) for layer in game_world.world for obj in layer)
        if hoe_exists:
            self.image.clip_draw(0, 50, 15, 15, self.x, self.y, 50, 50)
            draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def get_bb(self):
        return self.x-23,self.y-23,self.x+23,self.y+23
        pass

    def handle_collision(self, group, other):
        if group == 'water:water':
            game_world.remove_object(self)


class Seed:
    image = None

    def __init__(self, x, y):
        if Seed.image == None:
            Seed.image = load_image('resource/crops.png')
        self.x, self.y = x, y

    def draw(self):
        self.image.clip_draw(0, 1024 - 45, 18, 40, self.x, self.y, 18 * 2, 40 * 2)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def get_bb(self):
        return self.x - 23, self.y - 23, self.x + 23, self.y + 23
        pass

    def handle_collision(self, group, other):
        if group == 'seed:seed':
            pass
