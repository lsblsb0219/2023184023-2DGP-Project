import game_framework
from pico2d import *

import game_world
import item_mode
import title_mode
import item
from map import Ground, House
from girl import Girl

def init():
    global girl

    map = Ground()
    game_world.add_object(map, 0)

    girl = Girl()
    game_world.add_object(girl, 1)
    girl.x = 133
    girl.y = 380

    map2 = House()
    game_world.add_object(map2, 0)

    if girl.hoes: # 리스트가 비어있지 않다면
        for hoe in girl.hoes:
            game_world.add_collision_pair('hoe:hoe', None, hoe)

    game_world.add_collision_pair('girl:house', girl, map2)

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
    for layer in game_world.world:
        if girl in layer:  # 해당 레이어에 girl 객체가 있으면
            game_world.remove_object(girl)  # 삭제
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
