from myclass import *

def row_ideal_score(myarr, enemy: Board, action: list):
    ideal_utility = 0
    for i in range(1, 7):
        utility = deduction(myarr, enemy, action, i)
        if utility > ideal_utility:
            ideal_utility = utility
    return ideal_utility

def row_ideal_move(myarr, enemy: Board, action: list):
    ideal_utility = 0
    ideal_number = 0
    for i in range(1, 7):
        utility = deduction(myarr, enemy, action, i)
        if utility > ideal_utility:
            ideal_utility = utility
            ideal_number = i
    return ideal_number

def isOver(myarr: Board, enemy: Board):
    return myarr.isFull() or enemy.isFull()

def deduction(myarr: Board, enemy: Board, action: list, num: int):
    row = action[0]
    col = action[1]
    temp1 = copy.deepcopy(myarr)
    temp2 = copy.deepcopy(enemy)

    temp1.myarr[row][col] = num
    eliminate(temp2, row, num)
    temp1.update()
    temp2.update()

    my_inc = temp1.score_list[row] - myarr.score_list[row]
    ene_inc = temp2.score_list[row] - enemy.score_list[row]

    utility = my_inc - ene_inc

    return utility

def twice_deduction(myarr: Board, enemy: Board, action: list, num: int):
    row = action[0]
    col = action[1]
    temp1 = copy.deepcopy(myarr)
    temp2 = copy.deepcopy(enemy)

    temp1.myarr[row][col] = num
    eliminate(temp2, row, num)
    temp1.update()
    temp2.update()   # 准备进行二次演绎

    my_inc1 = temp1.score_list[row] - myarr.score_list[row]
    ene_inc1 = temp2.score_list[row] - enemy.score_list[row]

    now_utility = my_inc1 - ene_inc1

    next_action = [row, -1]
    for item in temp2.myarr:
        if item[0] == row:
            next_action[1] = item[1]
            break

    future_ideal_utility = row_ideal_score(temp2, temp1, next_action)

    total_utility = now_utility - future_ideal_utility   # 得到杠杆收益
    return total_utility

def eliminate(myarr: Board, row: int, num: int):
    line = myarr.myarr[row]
    for i in range(0, 3):
        if line[i] == num:
            line[i] = 0
    myarr.myarr[row] = line