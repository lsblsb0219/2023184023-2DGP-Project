from pico2d import load_image, draw_rectangle, get_canvas_width, get_canvas_height, clamp

import server

class Ground:
    # 생성자를 이용해서 객체의 초기 상태를 정의상태 정의
    def __init__(self):
        self.Ground_image = load_image('resource/ground.png')
        self.Sky_image = load_image('resource/sky.png')
        self.cw = get_canvas_width()
        self.ch = get_canvas_height()
        self.w = self.cw
        self.h = self.ch
        self.window_left = 0
        self.window_bottom = 0

    def update(self):
        self.window_left = clamp(0, int(server.girl.x) - self.cw // 2, self.w - self.cw - 1)
        self.window_bottom = clamp(0, int(server.girl.y) - self.ch // 2, self.h - self.ch - 1)
        pass

    def draw(self):
        self.Sky_image.draw(300, 500, 1000, 300)
        self.Ground_image.draw(640, 180)


class House:
    def __init__(self):
        self.House_image = load_image('resource/houses.png')
        self.x, self.y = 200, 480
        self.cw = get_canvas_width()
        self.ch = get_canvas_height()
        self.w = self.House_image.w
        self.h = self.House_image.h
        self.window_left = 0
        self.window_bottom = 0

    def update(self):
        self.window_left = clamp(0, int(server.girl.x) - self.cw // 2, self.w - self.cw - 1)
        self.window_bottom = clamp(0, int(server.girl.y) - self.ch // 2, self.h - self.ch - 1)
        pass

    def draw(self):
        # 432//3 = 144
        self.House_image.clip_draw(0, 432 - 144, 272, 144, 200, 480, 272 * 2, 144 * 2)
        draw_rectangle(*self.get_bb())
        pass

    def get_bb(self):
        return self.x-200,self.y-55,self.x+50,self.y+150
        pass

    def handle_collision(self, group, other):
        if group == 'girl:house':
            pass


class HouseIn:
    def __init__(self):
        self.HouseIn_background = load_image('resource/black.png')
        self.HouseIn_image = load_image('resource/houseIn.png')
        self.x, self.y = 400, 300
        self.cw = get_canvas_width()
        self.ch = get_canvas_height()
        self.w = self.cw
        self.h = self.ch
        self.window_left = 0
        self.window_bottom = 0

    def update(self):
        self.window_left = clamp(0, int(server.girl.x) - self.cw // 2, self.w - self.cw - 1)
        self.window_bottom = clamp(0, int(server.girl.y) - self.ch // 2, self.h - self.ch - 1)

        pass

    def draw(self):
        self.HouseIn_background.draw(self.x, self.y)
        self.HouseIn_image.draw(self.x, self.y)
        pass



class Door:
    def __init__(self):
        self.image = load_image('resource/black.png')
        self.x = 300
        self.y = 20

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y, 10, 10)
        x1, y1, x2, y2 = self.get_bb()
        draw_rectangle(x1 - server.map.window_left, y1 - server.map.window_bottom,
                       x2 - server.map.window_left, y2 - server.map.window_bottom)

        pass

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def handle_collision(self, group, other):
        if group == 'girl:door':
            pass