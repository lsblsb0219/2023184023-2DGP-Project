from pico2d import load_image, draw_rectangle

import game_world
import item
from game_world import collide
from item import Hoe
from mouse import handle_mouse_events
from state_machine import *

class Idle:
    @staticmethod
    def enter(girl, e):
        if start_event(e) or up_down(e) or down_up(e):  # 앞
            girl.action = 12
            girl.yface_dir = 1
        elif down_down(e) or up_up(e): # 뒤
            girl.action = 10
            girl.yface_dir = -1
        elif right_down(e) or left_up(e): # 왼쪽
            girl.action = 9
            girl.xface_dir = -1
        elif left_down(e) or right_up(e): # 오른쪽
            girl.action = 11
            girl.xface_dir = 1

        girl.frame = 0

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
        girl.image.clip_draw(girl.frame * 16, girl.action * 32, 16, 32, girl.x, girl.y, 16 * 3, 32 * 3)


class Run:
    @staticmethod
    def enter(girl, e):
        if right_down(e) or left_up(e):  # 오른쪽으로 RUN
            girl.dir, girl.xface_dir, girl.yface_dir, girl.action = 1, 1, 0, 11
        elif left_down(e) or right_up(e):  # 왼쪽으로 RUN
            girl.dir, girl.xface_dir, girl.yface_dir, girl.action = -1, -1, 0, 9
        elif down_down(e) or up_up(e): # 아래로 RUN
            girl.dir, girl.xface_dir, girl.yface_dir, girl.action = -1, 0, -1, 12
        elif up_down(e) or down_up(e): # 위로 RUN
            girl.dir, girl.xface_dir, girl.yface_dir, girl.action = 1, 0, 1, 10

    @staticmethod
    def exit(girl, e):
        pass

    @staticmethod
    def do(girl):
        girl.frame_time_accumulator += 1
        if girl.frame_time_accumulator >= girl.frame_time_update_interval:
            girl.frame = (girl.frame + 1) % 4
            girl.frame_time_accumulator = 0

        if girl.yface_dir == 0:
            if 0 < girl.x + girl.dir * 2 < 800:
                girl.x += girl.dir * 0.5
        elif girl.xface_dir == 0:
            if 140 < girl.y + girl.dir * 2 < 400:
                girl.y += girl.dir * 0.5
        pass

    @staticmethod
    def draw(girl):
            girl.image.clip_draw(girl.frame * 16, girl.action * 32, 16, 32, girl.x, girl.y, 16 * 3, 32 * 3)


class Girl:
    def __init__(self):
        self.x, self.y = 400, 300
        self.xface_dir, self.yface_dir = 1, 1
        self.frame_time_accumulator = 0 # 누적 시간
        self.frame_time_update_interval = 30 # 프레임 업데이트 간격
        self.image = load_image('Haley.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start(Idle)
        self.state_machine.set_transitions(
            {
                Idle: {down_down: Run, up_down: Run, down_up: Run, up_up: Run, right_down: Run, left_down: Run, left_up: Run, right_up: Run, click_l_down:Idle},
                Run: {down_down: Idle, up_down: Idle, down_up: Idle, up_up: Idle, right_down: Idle, left_down: Idle, right_up: Idle, left_up: Idle}
            }
        )
        self.item = None
        self.hoes = []

    def update(self):
        self.state_machine.update()
        #handle_mouse_events()

    def handle_event(self, event):
        # 여기서 받을 수 있는 것만 걸러야 함. right left  등등..
        self.state_machine.add_event(('INPUT', event))
        pass

    def draw(self):
        self.state_machine.draw()
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return  self.x - 25, self.y - 50, self.x + 25, self.y + 30

    def select_item(self):
        if self.xface_dir == 0:
            if self.yface_dir == -1: # 위쪽
                if self.item == 'Hoe':
                    select_item = hoe = Hoe(self.x, self.y, self.xface_dir, self.yface_dir)

                    for existing_hoe in self.hoes:
                        if collide(hoe, existing_hoe):
                            return

                    self.hoes.append(hoe)
                    game_world.add_objects([select_item], 1)
                    game_world.add_collision_pair('hoe:hoe', hoe, None)
                elif self.item == 'water':
                    pass

            elif self.yface_dir == 1: # 아래쪽(정면)
                if self.item == 'Hoe':
                    select_item = hoe = Hoe(self.x, self.y - 80, self.xface_dir, self.yface_dir)

                    for existing_hoe in self.hoes:
                        if collide(hoe, existing_hoe):
                            return

                    self.hoes.append(hoe)
                    game_world.add_objects([select_item], 1)
                    game_world.add_collision_pair('hoe:hoe', hoe, None)
                elif self.item == 'water':
                    pass

        elif self.yface_dir == 0:
            if self.xface_dir == -1: # 왼쪽
                if self.item == 'Hoe':
                    select_item = hoe = Hoe(self.x - 40, self.y - 40, self.xface_dir, self.yface_dir)

                    for existing_hoe in self.hoes:
                        if collide(hoe, existing_hoe):
                            return

                    self.hoes.append(hoe)
                    game_world.add_objects([select_item], 1)
                    game_world.add_collision_pair('hoe:hoe', hoe, None)
                elif self.item == 'water':
                    pass

            elif self.xface_dir == 1: # 오른쪽
                if self.item == 'Hoe':
                    select_item = hoe = Hoe(self.x + 40, self.y - 40, self.xface_dir, self.yface_dir)

                    for existing_hoe in self.hoes:
                        if collide(hoe, existing_hoe):
                            return

                    self.hoes.append(hoe)
                    game_world.add_objects([select_item], 1)
                    game_world.add_collision_pair('hoe:hoe', hoe, None)
                elif self.item == 'water':
                    pass

        return self.hoes
