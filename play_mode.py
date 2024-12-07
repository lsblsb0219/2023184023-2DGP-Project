import game_framework
from pico2d import *

import game_world
import item_mode
import server
import title_mode

from map import Ground, House
from girl import Girl
from music import Music

def init():
    server.music = Music()
    server.music.init()

    server.map = Ground()
    game_world.add_object(server.map, 0)

    if not hasattr(server, 'girl') or server.girl is None:
            server.girl = Girl()
    game_world.add_object(server.girl, 1)
    server.girl.x = 133
    server.girl.y = 380

    map2 = House()
    game_world.add_object(map2, 0)

    if server.girl.hoes: # 리스트가 비어있지 않다면
        for hoe in server.girl.hoes:
            game_world.add_collision_pair('hoe:hoe', None, hoe)

        if server.girl.waters:  # 리스트가 비어있지 않다면
            for water in server.girl.waters:
                game_world.add_collision_pair('water:water', None, water)

    if server.girl.seeds:
        for seed in server.girl.seeds:
            game_world.add_collision_pair('seed:seed', None, seed)

    game_world.add_collision_pair('girl:house', server.girl, map2)

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
    if server.music:
        server.music.finish()
    game_world.clear()


def update():
    game_world.update()
    game_world.handle_collisions()


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause():
    if server.music:
        server.music.finish()
    pass

def resume():
    if server.music:
        server.music.resume()
    pass
