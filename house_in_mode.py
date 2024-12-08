from pico2d import *

import day_time
import game_framework
import game_world
import item_mode
import title_mode
import server

from map import HouseIn, Door, Bed
from music import Music

def init():
    server.music = Music()
    server.music.init()

    server.map = HouseIn()
    game_world.add_object(server.map, 0)

    game_world.add_object(server.girl, 1)
    server.girl.x = 300
    server.girl.y = 100

    door = Door()
    game_world.add_object(door, 0)

    bed = Bed()
    game_world.add_object(bed, 0)

    game_world.add_collision_pair('girl:door', server.girl, door)
    game_world.add_collision_pair('girl:bed', server.girl, bed)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.change_mode(title_mode)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(title_mode)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_e:
            game_framework.push_mode(item_mode)
            if server.music:
                server.music.init()
        else:
            server.girl.handle_event(event)

def finish():
    if server.music:
        server.music.finish()
    game_world.clear()


def update():
    game_world.update()
    day_time.update_time()
    game_world.handle_collisions()




def draw():
    clear_canvas()
    game_world.render()
    day_time.draw_time()
    update_canvas()

def pause():
    if server.music:
        server.music.finish()
    pass

def resume():
    if server.music:
        server.music.resume()
    pass

