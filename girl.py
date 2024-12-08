import math

from pico2d import load_image, draw_rectangle, clamp, load_font
import game_framework
import game_world
import server
from game_world import collide
from item import Hoe, Water, Seed
from mouse import handle_mouse_events
from sound import SoundManager
from state_machine import *

# Girl Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 40.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Girl Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class Idle:
    @staticmethod
    def enter(girl, e):
        girl.frame = 0
        girl.speed = 0
        girl.dir = 0

    @staticmethod
    def exit(girl, e):
        if click_l_down(e):
            girl.select_item()
        pass

    @staticmethod
    def do(girl):
        pass

    @staticmethod
    def draw(girl):
        girl.image.clip_draw(int(girl.frame * 16), int(girl.action * 32), 16, 32, int(girl.x), int(girl.y), 16 * 3, 32 * 3)


class RunRight:
    @staticmethod
    def enter(girl, e):
        girl.action = 11
        girl.speed = RUN_SPEED_PPS
        girl.dir = 0

    @staticmethod
    def exit(girl, e):
        pass

    @staticmethod
    def do(girl):
        pass


class RunRightUp:
    @staticmethod
    def enter(girl, e):
        girl.action = 11
        girl.speed = RUN_SPEED_PPS
        girl.dir = math.pi / 4.0

    @staticmethod
    def exit(girl, e):
        pass

    @staticmethod
    def do(girl):
        pass


class RunRightDown:
    @staticmethod
    def enter(girl, e):
        girl.action = 11
        girl.speed = RUN_SPEED_PPS
        girl.dir = -math.pi / 4.0

    @staticmethod
    def exit(girl, e):
        pass

    @staticmethod
    def do(girl):
        pass


class RunLeft:
    @staticmethod
    def enter(girl, e):
        girl.action = 9
        girl.speed = RUN_SPEED_PPS
        girl.dir = math.pi

    @staticmethod
    def exit(girl, e):
        pass

    @staticmethod
    def do(girl):
        pass


class RunLeftUp:
    @staticmethod
    def enter(girl, e):
        girl.action = 9
        girl.speed = RUN_SPEED_PPS
        girl.dir = math.pi * 3.0 / 4.0

    @staticmethod
    def exit(girl, e):
        pass

    @staticmethod
    def do(girl):
        pass


class RunLeftDown:
    @staticmethod
    def enter(girl, e):
        girl.action = 9
        girl.speed = RUN_SPEED_PPS
        girl.dir = - math.pi * 3.0 / 4.0

    @staticmethod
    def exit(girl, e):
        pass

    @staticmethod
    def do(girl):
        pass


class RunUp:
    @staticmethod
    def enter(girl, e):
        girl.action = 10
        girl.speed = RUN_SPEED_PPS
        girl.dir = math.pi / 2.0

    @staticmethod
    def exit(girl, e):
        pass

    @staticmethod
    def do(girl):
        pass


class RunDown:
    @staticmethod
    def enter(girl, e):
        girl.action = 12
        girl.speed = RUN_SPEED_PPS
        girl.dir = - math.pi / 2.0
        pass

    @staticmethod
    def exit(girl, e):
        pass

    @staticmethod
    def do(girl):
        pass


class Girl:
    def __init__(self):
        self.sound_manager = SoundManager()
        self.x = server.map.w / 2
        self.y = server.map.h / 2
        self.frame = 0
        self.action = 3
        self.frame_time_accumulator = 0 # 누적 시간
        self.frame_time_update_interval = 30 # 프레임 업데이트 간격
        self.image = load_image('resource/Haley.png')
        self.font = load_font('resource/ENCR10B.TTF', 18)
        self.state_machine = StateMachine(self)
        self.state_machine.start(Idle)
        self.state_machine.set_transitions(
            {
                Idle: {right_down: RunRight, left_down: RunLeft, left_up: RunRight, right_up: RunLeft,
                       upkey_down: RunUp, downkey_down: RunDown, upkey_up: RunDown, downkey_up: RunUp, click_l_down:Idle},
                RunRight: {right_up: Idle, left_down: Idle, upkey_down: RunRightUp, upkey_up: RunRightDown,
                           downkey_down: RunRightDown, downkey_up: RunRightUp},
                RunRightUp: {upkey_up: RunRight, right_up: RunUp, left_down: RunUp, downkey_down: RunRight},
                RunUp: {upkey_up: Idle, left_down: RunLeftUp, downkey_down: Idle, right_down: RunRightUp,
                        left_up: RunRightUp, right_up: RunLeftUp},
                RunLeftUp: {right_down: RunUp, downkey_down: RunLeft, left_up: RunUp, upkey_up: RunLeft},
                RunLeft: {left_up: Idle, upkey_down: RunLeftUp, right_down: Idle, downkey_down: RunLeftDown,
                          upkey_up: RunLeftDown, downkey_up: RunLeftUp},
                RunLeftDown: {left_up: RunDown, downkey_up: RunLeft, upkey_down: RunLeft, right_down: RunDown},
                RunDown: {downkey_up: Idle, left_down: RunLeftDown, upkey_down: Idle, right_down: RunRightDown,
                          left_up: RunRightDown, right_up: RunLeftDown},
                RunRightDown: {right_up: RunDown, downkey_up: RunRight, left_down: RunDown, upkey_down: RunRight}
            }
        )
        self.frame = 4
        self.action = 12
        self.item = None
        self.hoes = []
        self.waters = []
        self.seeds = []

    def update(self):
        self.state_machine.update()
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * server.frame_time) % 4
        if self.state_machine.cur_state == Idle:
            self.frame = 0

        self.x += math.cos(self.dir) * self.speed * server.frame_time
        self.y += math.sin(self.dir) * self.speed * server.frame_time

        self.x = clamp(
            10.0,
            self.x,
            server.map.w - 25.0
        )
        self.y = clamp(
            30.0,
            self.y,
            server.map.h - 0.0)

        # handle_mouse_events()

    def handle_event(self, event):
        # 여기서 받을 수 있는 것만 걸러야 함. right left  등등..
        self.state_machine.add_event(('INPUT', event))
        if self.item is not None and event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            self.sound_manager.play_item_sound(self.item)
        pass

    def draw(self):
        self.sx = self.x - server.map.window_left
        self.sy = self.y - server.map.window_bottom

        self.image.clip_draw(int(self.frame) * 16, self.action * 32, 16, 32, self.sx, self.sy, 16 * 3, 32 * 3)

        x1, y1, x2, y2 = self.get_bb()
        draw_rectangle(x1 - server.map.window_left, y1 - server.map.window_bottom,
                       x2 - server.map.window_left, y2 - server.map.window_bottom)

        self.font.draw(self.sx - 100, self.sy + 60, f'({self.sx:.2f}, {self.sy:.2f})', (255, 255, 0))

    def get_bb(self):
        return  self.x - 25, self.y - 50, self.x + 25, self.y + 30

    # 상태 저장 함수
    def save_state(self):
        saved_hoes = [(hoe.x, hoe.y) for hoe in self.hoes]
        saved_waters = [(water.x, water.y) for water in self.waters]
        saved_seeds = [(seed.x, seed.y) for seed in self.seeds]
        return saved_hoes, saved_waters, saved_seeds

    # 상태 복원 함수
    def restore_state(self, saved_hoes, saved_waters, saved_seeds):
        self.hoes = [Hoe(x, y) for x, y in saved_hoes]
        self.waters = [Water(x, y) for x, y in saved_waters]
        self.seeds = [Seed(x, y) for x, y in saved_seeds]

    def select_item(self):
        if self.item == 'Water':
            if not self.hoes:
                return

            water_x, water_y = self.x, self.y

            for existing_hoe in self.hoes:
                if collide(self, existing_hoe):  # 충돌하는 Hoe를 찾음
                    water_x, water_y = existing_hoe.x, existing_hoe.y
                    self.hoes.remove(existing_hoe)
                    break

            select_item = water = Water(water_x, water_y)
            for existing_water in self.waters:
                if collide(water, existing_water):
                    return

            self.waters.append(water)
            game_world.add_objects([select_item], 1)
            game_world.add_collision_pair('water:water', water, None)

        if  self.item == 'Seed':
            if not self.hoes and not self.waters:
                return

            seed_x, seed_y = self.x, self.y

            for existing_hoe in self.hoes:
                if collide(self, existing_hoe):
                    seed_x, seed_y = existing_hoe.x, existing_hoe.y
                    break

            for existing_water in self.waters:
                if collide(self, existing_water):
                    seed_x, seed_y = existing_water.x, existing_water.y
                    break

            select_item = seed = Seed(seed_x, seed_y)

            for existing_seed in self.seeds:
                if collide(seed, existing_seed):
                    return

            self.seeds.append(seed)
            game_world.add_objects([select_item], 2)
            game_world.add_collision_pair('seed:seed', seed, None)


        if self.action == 10: # 위쪽
            if self.item == 'Hoe':
                select_item = hoe = Hoe(self.x, self.y)

                for existing_hoe in self.hoes:
                    if collide(hoe, existing_hoe):
                        return

                self.hoes.append(hoe)
                game_world.add_objects([select_item], 1)
                game_world.add_collision_pair('hoe:hoe', hoe, None)
                pass

        elif self.action == 12: # 아래쪽(정면)
            if self.item == 'Hoe':
                select_item = hoe = Hoe(self.x, self.y - 80)

                for existing_hoe in self.hoes:
                    if collide(hoe, existing_hoe):
                        return

                self.hoes.append(hoe)
                game_world.add_objects([select_item], 1)
                game_world.add_collision_pair('hoe:hoe', hoe, None)
                pass

        if self.action == 9: # 왼쪽
            if self.item == 'Hoe':
                select_item = hoe = Hoe(self.x - 40, self.y - 40)

                for existing_hoe in self.hoes:
                    if collide(hoe, existing_hoe):
                        return

                self.hoes.append(hoe)
                game_world.add_objects([select_item], 1)
                game_world.add_collision_pair('hoe:hoe', hoe, None)

                pass

        elif self.action == 11: # 오른쪽
            if self.item == 'Hoe':
                select_item = hoe = Hoe(self.x + 40, self.y - 40)

                for existing_hoe in self.hoes:
                    if collide(hoe, existing_hoe):
                        return

                self.hoes.append(hoe)
                game_world.add_objects([select_item], 1)
                game_world.add_collision_pair('hoe:hoe', hoe, None)
                pass



        return self.hoes

    def handle_collision(self, group, other):
        import house_in_mode
        import play_mode
        if group == 'girl:house':
            game_framework.change_mode(house_in_mode)
        if group == 'girl:door':
            game_framework.change_mode(play_mode)