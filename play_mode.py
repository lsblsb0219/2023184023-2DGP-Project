import game_framework
from pico2d import *

import game_world
import title_mode
from map import Ground
from girl import Girl

def init():
    global girl
    map = Ground()
    game_world.add_object(map, 0)
    girl = Girl()
    game_world.add_object(girl, 1)

def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.change_mode(title_mode)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(title_mode)
        else:
            girl.handle_event(event)

def finish():
    game_world.clear()

def update():
    game_world.update()

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause():
    pass

def resume():
    pass