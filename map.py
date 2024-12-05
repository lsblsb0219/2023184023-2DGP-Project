from pico2d import load_image, draw_rectangle, get_canvas_width, get_canvas_height, clamp
import server

class Ground:
    # 생성자를 이용해서 객체의 초기 상태를 정의상태 정의
    def __init__(self):
        self.Ground_image = load_image('ground.png')
        self.Sky_image = load_image('sky.png')
        self.cw = get_canvas_width()
        self.ch = get_canvas_height()
        self.w = self.Ground_image.w
        self.h = self.Ground_image.h

    def update(self):
        self.window_left = clamp(0, int(server.girl.x) - self.cw // 2, self.w - self.cw - 1)
        self.window_bottom = clamp(0, int(server.girl.y) - self.ch // 2, self.h - self.ch - 1)
        pass

    def draw(self):
        self.Sky_image.draw(300, 500, 1000, 300)
        self.Ground_image.draw(640, 180)


class House:
    def __init__(self):
        self.House_image = load_image('houses.png')
        self.x, self.y = 200, 480
        self.cw = get_canvas_width()
        self.ch = get_canvas_height()
        self.w = self.House_image.w
        self.h = self.House_image.h

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
        self.HouseIn_background = load_image('black.png')
        self.HouseIn_image = load_image('houseIn.png')
        self.x, self.y = 400, 300
        self.cw = get_canvas_width()
        self.ch = get_canvas_height()
        self.w = self.HouseIn_image.w
        self.h = self.HouseIn_image.h

    def update(self):
        self.window_left = clamp(0, int(server.girl.x) - self.cw // 2, self.w - self.cw - 1)
        self.window_bottom = clamp(0, int(server.girl.y) - self.ch // 2, self.h - self.ch - 1)
        pass

    def draw(self):
        self.HouseIn_background.draw(self.x, self.y)
        self.HouseIn_image.draw(self.x, self.y)
        pass

    def get_bb(self):
        pass

    def handle_collision(self, group, other):
        pass
