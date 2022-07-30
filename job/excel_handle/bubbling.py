# coding=utf-8
import random  # 随机数


class Bububble:
    def __init__(self):
        self.num_list = []

    def get_data_list(self):
        for i in range(20):
            ran = random.randint(1, 10000)
            if ran % 2 == 0:
                self.num_list.append(ran)
        print "偶数随机数组：", self.num_list

    def bubble_sort(self):
        for i in range(1, len(self.num_list)):
            for j in range(0, len(self.num_list) - i):
                if self.num_list[j] > self.num_list[j + 1]:
                    self.num_list[j], self.num_list[j + 1] = self.num_list[j + 1], self.num_list[j]
        print "冒泡排序结果：", self.num_list


if __name__ == '__main__':
    bubble = Bububble()
    bubble.get_data_list()
    bubble.bubble_sort()