from pico2d import *


class Hoe:
    image = None

    def __init__(self, x, y, xface_dir, yface_dir):
        if Hoe.image == None:
            Hoe.image = load_image('hoeDirt.png')
        self.x, self.y, self.xface_dir, self.yface_dir = x, y, xface_dir, yface_dir

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def get_bb(self):
        return self.x-10,self.y-10,self.x+10,self.y+10
        pass