from pico2d import *

import random

# Game object class here
class Ground:
    # 생성자를 이용해서 객체의 초기 상태를 정의상태 정의
    def __init__(self):
        self.image = load_image('ground.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(640, 180)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def update_world():
    for o in world:
        o.update()

def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()

def reset_world():
    global running
    global ground
    global world

    running = True
    world = []

    ground = Ground() # Grass 라는 클래스를 이용해서 grass 객체를 생성
    world.append(ground)

open_canvas()

# initialization code
reset_world()

# game main loop code
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)


# finalization code

close_canvas()
