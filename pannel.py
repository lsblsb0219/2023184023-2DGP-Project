from pico2d import load_image

class Pannel:
    def __init__(self):
        self.image = load_image('resource/inventory.png')

    def draw(self):
        self.image.draw(400, 300, 400, 80)

    def update(self):
        pass