from pico2d import *

import game_framework
import game_world
import item_mode
import title_mode
from map import HouseIn, Door
import server


def init():
    server.map = HouseIn()
    game_world.add_object(server.map, 0)

    game_world.add_object(server.girl, 1)
    server.girl.x = 300
    server.girl.y = 100

    door = Door()
    game_world.add_object(door, 0)

    game_world.add_collision_pair('girl:door', server.girl, door)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.change_mode(title_mode)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(title_mode)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_e:
            game_framework.push_mode(item_mode)
        else:
            server.girl.handle_event(event)

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
