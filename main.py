from functions import*
from myclass import *
from actions import *

if __name__ == '__main__':
    win_cnt = 0
    cnt = 1000
    for i in range(0, cnt):
        if i % 1000 == 0:
            print(f"alreadyplay:{i}")
        # if game_ai_vs_ai() == 1:
        #     win_cnt += 1
        if i == cnt - 1:
            print(f"alreadyplay:{i+1}")
        modeai = 0
        if game_ai_vs_random(modeai) == 1:
            win_cnt += 1
    win_rate = float(win_cnt)/cnt
    print(f"Wins_rate: {win_rate}")
