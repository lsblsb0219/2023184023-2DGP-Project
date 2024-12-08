from pico2d import *
import server


time_paused = False

def reset_time():
    # 인게임 시간 변수
    global game_minutes, elapsed_time, game_day
    game_minutes = 0
    elapsed_time = 0  # 경과 시간 누적
    game_day = 0

def pause_time():
    global time_paused
    time_paused = True

def resume_time():
    global time_paused
    time_paused = False

def update_time():
    global game_minutes, elapsed_time, game_day

    if time_paused:
        return

    elapsed_time += server.frame_time  # 경과 시간을 누적

    if elapsed_time >= 10:  # 60초가 지나면
        game_minutes += 1
        if game_minutes >= 3:  # 20분이 되면 초기화
            game_minutes = 0
            game_day += 1
        elapsed_time = 0  # 초 단위 누적 시간 초기화


def draw_time():
    font = load_font('resource/ENCR10B.TTF', 20)  # 폰트 로드
    font.draw(400, 550, f"Game Time: {game_day:02d} day {game_minutes:02d} minutes", (255, 255, 255))  # 흰색 텍스트로 출력
