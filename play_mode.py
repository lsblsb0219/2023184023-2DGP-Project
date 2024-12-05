import game_framework
from pico2d import *

import game_world
import item_mode
import server
import title_mode

from map import Ground, House
from girl import Girl

def init():
    server.map = Ground()
    game_world.add_object(server.map, 0)

    server.girl = Girl(server.map.w/2, server.map.h/2)
    game_world.add_object(server.girl, 1)
    server.girl.x = 133
    server.girl.y = 380

    map2 = House()
    game_world.add_object(map2, 0)

    if server.girl.hoes: # 리스트가 비어있지 않다면
        for hoe in server.girl.hoes:
            game_world.add_collision_pair('hoe:hoe', None, hoe)

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
    game_world.clear()
    for layer in game_world.world:
        if server.girl in layer:  # 해당 레이어에 girl 객체가 있으면
            game_world.remove_object(server.girl)  # 삭제
            break  # 삭제 후 루프 종료

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
