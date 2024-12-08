import day_time
import game_framework
from pico2d import*

import server
import play_mode

from music import Music

def init():
    global image
    image = load_image('resource/title.png')
    server.music = Music()
    server.music.init()
    day_time.reset_time()
    day_time.pause_time()

def finish():
    global image
    del image
    if server.music:
        server.music.finish()

def update():
    pass

def draw():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RETURN:
            game_framework.change_mode(play_mode)

def pause():
    if server.music:
        server.music.finish()
    pass

def resume():
    if server.music:
        server.music.resume()
    pass