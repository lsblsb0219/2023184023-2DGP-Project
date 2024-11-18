from pico2d import load_image
from state_machine import *

class Idle:
    @staticmethod
    def enter(girl, e):
        if start_event(e):
            girl.action = 12
            girl.xface_dir = 1
        elif right_down(e) or left_up(e):
            girl.action = 9
            girl.xface_dir = -1
        elif left_down(e) or right_up(e):
            girl.action = 11
            girl.xface_dir = 1

        girl.frame = 0

    @staticmethod
    def exit(girl, e):
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
            girl.dir, girl.xface_dir, girl.action = 1, 1, 11
        elif left_down(e) or right_up(e):  # 왼쪽으로 RUN
            girl.dir, girl.xface_dir, girl.action = -1, -1, 9

    @staticmethod
    def exit(girl, e):
        pass


    @staticmethod
    def do(girl):
        girl.frame = (girl.frame + 1) % 4
        if 0 < girl.x + girl.dir * 2 < 800:
            girl.x += girl.dir * 2
        pass

    @staticmethod
    def draw(girl):
        girl.image.clip_draw(girl.frame * 16, girl.action * 32, 16, 32, girl.x, girl.y, 16 * 3, 32 * 3)



class Girl:
    def __init__(self):
        self.x, self.y = 400, 300
        self.xface_dir, self.yface_dir = 1, 1
        self.image = load_image('Haley.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start(Idle)
        self.state_machine.set_transitions(
            {
                Idle: {right_down: Run, left_down: Run, left_up: Run, right_up: Run},
                Run: {right_down: Idle, left_down: Idle, right_up: Idle, left_up: Idle},
            }
        )

    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
        # 여기서 받을 수 있는 것만 걸러야 함. right left  등등..
        self.state_machine.add_event(('INPUT', event))
        pass

    def draw(self):
        self.state_machine.draw()