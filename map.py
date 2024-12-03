from pico2d import load_image

class Ground:
    # 생성자를 이용해서 객체의 초기 상태를 정의상태 정의
    def __init__(self):
        self.Ground_image = load_image('ground.png')
        self.Sky_image = load_image('sky.png')

    def update(self):
        pass

    def draw(self):
        self.Sky_image.draw(300, 500, 1000, 300)
        self.Ground_image.draw(640, 180)

