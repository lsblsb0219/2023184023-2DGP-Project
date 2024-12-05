from pico2d import *

import game_framework
import game_world
import item_mode
import play_mode
import title_mode
from map import HouseIn
import server


def init():
    server.map = HouseIn()
    game_world.add_object(server.map, 0)

  
    server.girl = server.girl(server.map.w/2, server.map.h/2)
    game_world.add_object(server.girl, 1)
    server.girl.x = 300
    server.girl.y = 100

    game_world.add_collision_pair('server.girl:houseIn', server.girl, map)

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
        if server.girl in layer:  # 해당 레이어에 server.girl 객체가 있으면
            game_world.remove_object(server.girl)  # 삭제
            break  # 삭제 후 루프 종료

def update():
    game_world.update()
    game_world.handle_collisions()

    if server.girl.x >= 290 and server.girl.x <= 310 and server.girl.y <= 90:
        game_framework.change_mode(play_mode)


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause():
    pass

def resume():
    pass

