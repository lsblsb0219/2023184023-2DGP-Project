from pico2d import *


mouse_x, mouse_y = 0, 0

def handle_mouse_events():
    global mouse_x, mouse_y
    events = get_events()
    for event in events:
        if event.type == SDL_MOUSEMOTION:  # 마우스가 움직일 때
            mouse_x, mouse_y = event.x, get_canvas_height() - event.y
            print(f'({mouse_x}, {mouse_y})')  # 좌표 출력
        elif event.type == SDL_MOUSEBUTTONDOWN:
            pass

    return mouse_x, mouse_y
