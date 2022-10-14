import copy
from functions import*

class Board:
    myarr = None
    score_list = list()
    spare_list = list()

    def __init__(self, arr):
        self.myarr = copy.deepcopy(arr)   # 初始化myarr

    def update(self):
        self.spare_list = list()
        self.score_list = list()
        for line in self.myarr:
            score_row = 0
            num_list = [0, 0, 0, 0, 0, 0, 0]
            for each in line:
                num_list[each] += 1
            for i in range(1, 7):
                if num_list[i] > 0:
                    score_row += i * pow(num_list[i], 2)
            self.score_list.append(score_row)

        for row in range(0, 3):
            for col in range(0, 3):
                if self.myarr[row][col] == 0:
                    self.spare_list.append([row, col])

    def score(self):
        total = 0
        for row in self.score_list:
            total += row
        return total

    def isFull(self):
        flag = True
        for line in self.myarr:
            for each in line:
                if each == 0:
                    flag = False
                    break
            if flag == False:
                break
        return flag

    def print_arr(self):
        for line in self.myarr:
            for each in line:
                print("%-3d" % each, end='')
            print("")
        print("")

    def cnt_spare(self):
        cnt_row = list()
        for i in range(0, 3):
            cnt_row.append(0)
        for each in self.spare_list:
            cnt_row[each[0]] += 1
        return cnt_row

    def get_row_state(self, row: int):
        cnt_row = self.cnt_spare()
        if cnt_row[row] > 0:
            return True
        else:
            return False


if __name__ == '__main__':
    arr = [[1, 2, 3], [5, 0, 6], [1 ,0, 6]]
    ene = [[2, 2, 1], [4, 5, 0], [1 ,4, 6]]
    b1 = Board(arr)
    b1.update()
    b2 = Board(ene)
    b2.update()
    utility = deduction(b1, b2, [2, 1], 6)
    print(utility)
    print(b1.score_list)
    score = b1.score()
    print(score)
    print(row_ideal_score(b1, b2, [1, 1], ))
    print(isOver(b1, b2))
    b1.print_arr()
    print(b1.spare_list)
    print(b1.cnt_spare())

    print("\n\n\n\n\n")

