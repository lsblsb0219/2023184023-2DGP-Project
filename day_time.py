from pico2d import *
import server


time_paused = False

def reset_time():
    # 인게임 시간 변수
    server.game_minutes = 0
    server.elapsed_time = 0  # 경과 시간 누적
    server.game_day = 0

def pause_time():
    global time_paused
    time_paused = True

def resume_time():
    global time_paused
    time_paused = False

def update_time():
    if time_paused:
        return

    server.elapsed_time += server.frame_time  # 경과 시간을 누적

    if server.elapsed_time >= 10:  # 60초가 지나면
        server.game_minutes += 1
        if server.game_minutes >= 3:  # 20분이 되면 초기화
            server.game_minutes = 0
            server.game_day += 1
        server.elapsed_time = 0  # 초 단위 누적 시간 초기화


def draw_time():
    font = load_font('resource/ENCR10B.TTF', 20)  # 폰트 로드
    font.draw(400, 550, f"Game Time: {server.game_day:02d} day {server.game_minutes:02d} minutes", (255, 255, 255))  # 흰색 텍스트로 출력
