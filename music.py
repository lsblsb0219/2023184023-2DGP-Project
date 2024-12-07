from pico2d import load_music

from game_framework import get_current_mode


class Music:
    def __init__(self):
        self.bgm = None

    def init(self):
        import house_in_mode
        import play_mode
        import title_mode

        if get_current_mode() == play_mode:
            self.bgm = load_music('resource/play_music.mp3')
        elif get_current_mode() == title_mode:
            self.bgm = load_music('resource/title_music.mp3')
        elif get_current_mode() == house_in_mode:
            self.bgm = load_music('resource/house_in_music.mp3')
        self.bgm.set_volume(30)  # 볼륨 설정 (0~128)
        self.bgm.repeat_play()   # 반복 재생

    def finish(self):
        if self.bgm:
            self.bgm.stop()  # 음악 정지

    def resume(self):
        if self.bgm:
            self.bgm.repeat_play()  # 음악 다시 재생
