import day_time
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
    day_time.resume_time() # 시간 다시 활성화


    server.music = Music()
    server.music.init()

    server.map = Ground()
    game_world.add_object(server.map, 0)

    if not hasattr(server, 'girl') or server.girl is None:
            server.girl = Girl()
    game_world.add_object(server.girl, 3)
    server.girl.x = 133
    server.girl.y = 380

    map2 = House()
    game_world.add_object(map2, 0)

    # 상태 복원
    server.girl.restore_state(server.saved_hoes, server.saved_waters, server.saved_seeds)

    # Hoe, Water, Seed 객체들을 game_world에 다시 추가
    if server.girl.hoes:  # 리스트가 비어있지 않다면
        for hoe in server.girl.hoes:
            # Hoe 객체가 복원된 위치에서 그려지도록 위치 설정
            hoe.x, hoe.y = hoe.saved_x, hoe.saved_y  # saved_x, saved_y는 복원된 값
            game_world.add_object(hoe, 1)
            game_world.add_collision_pair('hoe:hoe', None, hoe)

    if server.girl.waters:  # 리스트가 비어있지 않다면
        for water in server.girl.waters:
            # Water 객체가 복원된 위치에서 그려지도록 위치 설정
            water.x, water.y = water.saved_x, water.saved_y  # saved_x, saved_y는 복원된 값
            game_world.add_object(water, 1)
            game_world.add_collision_pair('water:water', None, water)

    if server.girl.seeds:  # 리스트가 비어있지 않다면
        for seed in server.girl.seeds:
            # Seed 객체가 복원된 위치에서 그려지도록 위치 설정
            seed.x, seed.y = seed.saved_x, seed.saved_y  # saved_x, saved_y는 복원된 값
            game_world.add_object(seed, 1)
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
            if server.music:
                server.music.init()
        else:
            server.girl.handle_event(event)

def finish():
    if server.music:
        server.music.finish()
    # 상태 저장
    server.saved_hoes, server.saved_waters, server.saved_seeds = server.girl.save_state()
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
