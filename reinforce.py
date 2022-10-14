from actions import*
from myclass import*
from utils import*
def decision_1(myarr: list, enemy: list, num: int):
    plot = spare(myarr)   # 找出此时棋盘上所有的空位
    cnt_row = cnt_spare(plot)
    best_action = list()
    best_action.append([-1, -1])   # 对最佳下法初始化
    max_utility = 0
    row_label = [0, 0, 0]
    for action in plot:
        if (row_label[action[0]] > 0):
            continue

        utility = deduction(myarr, enemy, action, num)
        if utility > max_utility:
            max_utility = utility
            best_action.clear()
            best_action.append(action)
        elif utility == max_utility:
            best_action.append(action)

        row_label[action[0]] = 1
    idx = -1
    leng = len(best_action)
    if leng > 1:
        empty_num = -1
        best = [-1, -1]
        for i in range(0, leng):
            if cnt_row[best_action[i][0]] > empty_num:
                empty_num = cnt_row[best_action[i][0]]
                best[0] = best_action[i][0]
                best[1] = best_action[i][1]
                idx = i
    else:
        best = best_action[0]


    # 当最好情况只有一种的时候，真的只能放“最好”的地方吗？
    if len(best_action) > 1:
        second_best = best_action[1 - idx]
    else:
        second_best = get_second_best(myarr, enemy, max_utility, num)
    if cnt_row[best[0]] == 1:   # 若最好的情况的对应行只有一个空位时
        ideal_utility = row_ideal_score(myarr, enemy, best)
        if max_utility < ideal_utility:   # 虽然当前下法是目前来看是最佳，但是如果我不这么下，未来可能可以获得更大的收益
            if second_best == [-1, -1]:   # 如果不存在次好的
                best_final = best
            else:
                other_utility = deduction(myarr, enemy, best, num)   # 平衡杠杆收益
                rate = 0.8   # 设置权衡指标，越大代表忍耐度越高
                tradeoff = rate * (ideal_utility - max_utility) - (1 - rate) * (max_utility - rate2 * other_utility)
                if tradeoff > 0:
                    best_final = second_best   # 先忍着，后面的更好
                else:
                    best_final = best   # 机不可失，时不再来
        else:
            temp1 = copy.deepcopy(myarr)
            temp2 = copy.deepcopy(enemy)   # 演绎，判断发生消去时是否会改变对方该行的状态
            state2_1 = get_row_state(temp2, best[0])
            Doit(temp1, temp2, best, num)
            state2_2 = get_row_state(temp2, best[0])
            if state2_1 != state2_2:
                enemy_row_spare = get_row_spare(temp2, best[0])
                if len(enemy_row_spare) == 1:
                    enemy_ideal_utility = row_ideal_score(temp2, temp1, enemy_row_spare[0])
                    two_utility = max_utility - enemy_ideal_utility
                    if two_utility > 0:
                        best_final = best
                    else:   # 大概率不能放这里，怎么做。万一对方达不到最优状态呢
                        if second_best == [-1, -1]:
                            best_final = best
                        else:
                            best_final = second_best
                else:
                    best_final = second_best
            else:
                best_final = best
    else:
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