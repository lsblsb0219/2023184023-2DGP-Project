from pico2d import *

import game_world


class Hoe:
    image = None

    def __init__(self, x, y):
        if Hoe.image == None:
            Hoe.image = load_image('resource/hoeDirt.png')
        self.x, self.y = x, y
        self.saved_x = x  # 상태 저장을 위한 위치
        self.saved_y = y  # 상태 저장을 위한 위치

    def save_state(self):
        # 상태 저장 시 위치 정보도 함께 저장
        return self.x, self.y

    def restore_state(self, saved_x, saved_y):
        # 상태 복원 시 위치 정보 설정
        self.x, self.y = saved_x, saved_y
        self.saved_x, self.saved_y = saved_x, saved_y  # 복원된 위치 저장

    def draw(self):
        self.image.clip_draw(0, 50, 15, 15, self.x, self.y, 50, 50)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def get_bb(self):
        return self.x-23,self.y-23,self.x+23,self.y+23
        pass

    def handle_collision(self, group, other):
        if group == 'hoe:hoe':
            game_world.remove_object(self)
        if group == 'hoe:water':
            game_world.remove_object(self)


class Water:
    image = None

    def __init__(self, x, y):
        if Water.image == None:
            Water.image = load_image('resource/hoeDirtDark.png')
        self.x, self.y = x, y
        self.saved_x = x  # 상태 저장을 위한 위치
        self.saved_y = y  # 상태 저장을 위한 위치

    def save_state(self):
        # 상태 저장 시 위치 정보도 함께 저장
        return self.x, self.y

    def restore_state(self, saved_x, saved_y):
        # 상태 복원 시 위치 정보 설정
        self.x, self.y = saved_x, saved_y
        self.saved_x, self.saved_y = saved_x, saved_y  # 복원된 위치 저장

    def draw(self):
        hoe_exists = any(isinstance(obj, Hoe) for layer in game_world.world for obj in layer)
        if hoe_exists:
            self.image.clip_draw(0, 50, 15, 15, self.x, self.y, 50, 50)
            draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def get_bb(self):
        return self.x-23,self.y-23,self.x+23,self.y+23
        pass

    def handle_collision(self, group, other):
        if group == 'water:water':
            game_world.remove_object(self)


class Seed:
    image = None

    def __init__(self, x, y, created_day=0):
        if Seed.image == None:
            Seed.image = load_image('resource/crops.png')
        self.x, self.y = x, y
        self.saved_x = x  # 상태 저장을 위한 위치
        self.saved_y = y  # 상태 저장을 위한 위치
        self.created_day = created_day # 씨앗 생성 날
        self.state = "growing" # 씨앗 상태 (처음)

    def save_state(self):
        # 상태 저장 시 위치 정보도 함께 저장
        return self.x, self.y

    def restore_state(self, saved_x, saved_y):
        # 상태 복원 시 위치 정보 설정
        self.x, self.y = saved_x, saved_y
        self.saved_x, self.saved_y = saved_x, saved_y  # 복원된 위치 저장

    def draw(self):
        if self.state == "growing":
            self.image.clip_draw(0, 1024 - 45, 18, 40, self.x, self.y, 18 * 2, 40 * 2)
        elif self.state == "grown":
            self.image.clip_draw(30, 1024 - 45, 18, 40, self.x, self.y, 18 * 2, 40 * 2)
        elif self.state == "ripe":
            self.image.clip_draw(80, 1024 - 40, 18, 40, self.x, self.y, 18 * 2, 40 * 2)
        draw_rectangle(*self.get_bb())

    def update(self):
        # 시간 경과에 따른 상태 변화
        import server
        days_since_creation = server.game_day - self.created_day

        if self.state == "growing" and days_since_creation >= 3:
            self.state = "grown"
        elif self.state == "grown" and days_since_creation >= 6:
            self.state = "ripe"
        pass

    def get_bb(self):
        return self.x - 23, self.y - 23, self.x + 23, self.y + 23
        pass

    def handle_collision(self, group, other):
        if group == 'seed:seed':
            pass
