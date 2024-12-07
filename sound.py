from pico2d import load_music

class SoundManager:
    def __init__(self):
        self.bgm = None

    def play_item_sound(self, item):
        # item에 따라 다른 소리 재생
        if item == 'Hoe':
            self._play_music('resource/hoe_sound.mp3')
        elif item == 'Water':
            self._play_music('resource/water_sound.mp3')
        elif item == 'Seed':
            self._play_music('resource/seed_sound.mp3')


    def _play_music(self, path):
        if self.bgm:
            self.bgm.stop()  # 기존 음악이 있다면 멈추기
        self.bgm = load_music(path)
        self.bgm.set_volume(30)
        self.bgm.play(1)  # 음악 재생
