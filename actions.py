from myclass import Board
from functions import *
import random
import copy

def nextStep(ownBoard, otherBoard, figure):
    myarr = list()   # 数据格式转化
    enemy = list()
    for i in range(0, 3):
        temp1 = list()
        temp2 = list()
        for j in range(0, 3):
            temp1.append(ownBoard[i * 3 + j])
            temp2.append(otherBoard[i * 3 + j])
        myarr.append(temp1)
        enemy.append(temp2)

    plot = list()  # 找出此时棋盘上所有的空位
    for row in range(0, 3):
        for col in range(0, 3):
            if myarr[row][col] == 0:
                plot.append([row, col])

    cnt_row = list()   # 求每行空位个数
    for i in range(0, 3):
        cnt_row.append(0)
    for each in plot:
        cnt_row[each[0]] += 1

    best_action = list()
    best_action.append([-1, -1])  # 对最佳下法初始化
    max_utility = 0
    row_label = [0, 0, 0]
    for action in plot:
        if (row_label[action[0]] > 0):
            continue
        utility = deduction(myarr, enemy, action, figure)
        if utility > max_utility:
            max_utility = utility
            best_action.clear()
            best_action.append(action)
        elif utility == max_utility:
            best_action.append(action)

        row_label[action[0]] = 1
    leng = len(best_action)
    if leng > 1:
        empty_num = -1
        best = [-1, -1]
        for i in range(0, leng):
            if cnt_row[best_action[i][0]] > empty_num:
                empty_num = cnt_row[best_action[i][0]]
                best[0] = best_action[i][0]
                best[1] = best_action[i][1]
    else:
        best = best_action[0]

    best_output = best[0] * 3 + best[1]   # 数据格式转化
    return best_output

def decision(myarr: Board, enemy: Board, num: int):

    plot = myarr.spare_list   # 找出此时棋盘上所有的空位
    cnt_row = myarr.cnt_spare()
    best_action = list()
    best_action.append([-1, -1])   # 对最佳下法初始化
    max_utility = 0
    row_label = [0, 0, 0]
    for action in plot:
        if (row_label[action[0]] > 0):   # 每行至多演绎一次
            continue
        utility = deduction(myarr, enemy, action, num)   # 演绎函数
        if utility > max_utility:
            max_utility = utility
            best_action.clear()
            best_action.append(action)
        elif utility == max_utility:
            best_action.append(action)   # 添加到可行解列表

        row_label[action[0]] = 1
    leng = len(best_action)
    if leng > 1:
        empty_num = -1
        best = [-1, -1]
        for i in range(0, leng):
            if cnt_row[best_action[i][0]] > empty_num:
                empty_num = cnt_row[best_action[i][0]]   # 在可行解列表中选取最优解
                best[0] = best_action[i][0]
                best[1] = best_action[i][1]
    else:
        best = best_action[0]

    best_final = best
    return best_final

def decision_reinforce(myarr: Board, enemy: Board, num: int):
    plot = myarr.spare_list   # 找出此时棋盘上所有的空位
    my_cnt_row = myarr.cnt_spare()
    enemy_cnt_row = enemy.cnt_spare()
    decisions = list()
    row_label = [0, 0, 0]
    for each_action in plot:
        if (row_label[each_action[0]]):
            continue

        utility = deduction(myarr, enemy, each_action, num)
        each_decision = dict()
        each_decision["utility"] = utility
        each_decision["action"] = each_action
        each_decision["space"] = my_cnt_row[each_action[0]]
        decisions.append(each_decision)
        row_label[each_action[0]] = 1   # 设置标志，下次跳过该行
    decisions.sort(key=lambda x: (-x['utility']))   # 对决策列表的收益值进行降序排列

    ext = list()   # 用来存放备选项的列表
    cons = list()  # 用来存放每一行好决策的列表

    for single_decision in decisions:
        action_temp = single_decision['action']
        row_temp = action_temp[0]

        if my_cnt_row[row_temp] == 2:   # 自己的这行快满（已有2个元素）
            if enemy_cnt_row[row_temp] == 3:   # 假设对方该行已满
                ideal_num = row_ideal_move(myarr, enemy, action_temp)
                numof1 = 0   # 获取该行1的数量
                for each in myarr.myarr[row_temp]:
                    if each == 1:
                        numof1 += 1
                if ideal_num == num and numof1 != 2:   # 排除[1, 1, 6]的特殊情况
                    cons.append(single_decision)
                    continue
                else:
                    ext.append(single_decision)   # 将该决策放入备选项队列，判断下一种情况
                    continue
            else:   # 假设对方该行未满
                ext.append(single_decision)
                continue
        else:   # 自己的这行未满（已有2个元素）
            cons.append(single_decision)
            continue

    if (len(cons) > 0):   # 可行解列表
        cons.sort(key=lambda x: (-x['utility'], -x['space']))   # 先收益后空间，猛冲
        best = cons[0]['action']
    else:   # 无可行解，差中选优
        ext.sort(key=lambda x: (-x['space'], -x['utility']))   # 先空间后收益，求稳
        best = ext[0]['action']

    return best

def Doit(myarr: Board, enemy: Board, action: list, num: int):
    row = action[0]
    col = action[1]
    myarr.myarr[row][col] = num
    eliminate(enemy, row, num)
    myarr.update()
    enemy.update()

def aiPlay(myarr: Board, enemy: Board, modeai: int):
    num = random.randint(1, 6)
    if modeai == 0:
        action = decision(myarr, enemy, num)
    elif modeai == -1:
        action = decision_reinforce(myarr, enemy, num)
    Doit(myarr, enemy, action, num)

def randomPlay(myarr: Board, enemy: Board):
    num = random.randint(1, 6)
    plot = myarr.spare_list
    random.shuffle(plot)
    action = plot[0]
    Doit(myarr, enemy, action, num)

def game_ai_vs_random(modeai: int):

    board_A = Board([])
    board_B = Board([])
    temp = [0] * 3

    for i in range(0, 3):
        board_A.myarr.append(copy.deepcopy(temp))
        board_B.myarr.append(copy.deepcopy(temp))

    board_A.update()
    board_B.update()

    while (True):
        if isOver(board_A, board_B):
            break
        aiPlay(board_A, board_B, modeai)
        if isOver(board_A, board_B):
            break
        randomPlay(board_B, board_A)
        if isOver(board_A, board_B):
            break

    board_A_score = board_A.score()
    board_B_score = board_B.score()

    if board_A_score > board_B_score:
        result_ai = 1
    elif board_A_score == board_B_score:
        result_ai = 0
    else:
        result_ai = -1

    return result_ai

def game_ai_vs_ai():
    board_A = Board([])
    board_B = Board([])
    temp = [0] * 3

    for i in range(0, 3):
        board_A.myarr.append(copy.deepcopy(temp))
        board_B.myarr.append(copy.deepcopy(temp))

    board_A.update()
    board_B.update()

    while (True):
        if isOver(board_A, board_B):
            break
        aiPlay(board_A, board_B, -1)
        if isOver(board_A, board_B):
            break
        aiPlay(board_B, board_A, 0)
        if isOver(board_A, board_B):
            break

    board_A_score = board_A.score()
    board_B_score = board_B.score()

    if board_A_score > board_B_score:
        result_ai = 1
    elif board_A_score == board_B_score:
        result_ai = 0
    else:
        result_ai = -1

    return result_ai