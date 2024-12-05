from pico2d import *

import game_framework
import game_world
import item_mode
import play_mode
import title_mode
from girl import Girl
from map import HouseIn


def init():
    global girl

    map = HouseIn()
    game_world.add_object(map, 0)

    girl = play_mode.girl
    game_world.add_object(girl, 1)

    game_world.add_collision_pair('girl:houseIn', girl, map)

def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.change_mode(title_mode)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(title_mode)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_e:
            game_framework.push_mode(item_mode)
        else:
            girl.handle_event(event)

def finish():
    game_world.clear()

def update():
    game_world.update()
    game_world.handle_collisions()


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause():
    pass

def resume():
    pass

