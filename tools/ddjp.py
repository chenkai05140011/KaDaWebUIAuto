# coding:utf-8
# @author:CHEN XIAO KAI
# @file:ke1
# @time:2022/6/2115:46
# @software:PyCharm
from ctypes import *
import time
import os
import win32api


class op_keyboard():

    def __init__(self):
        parentDirPath = os.path.dirname(os.path.abspath(__file__))
        path = parentDirPath + ("\\DD94687.64.dll")  # 这个dll是当前路径下面的
        print(path)
        self.dd_dll = windll.LoadLibrary(path)
        st = self.dd_dll.DD_btn(0)  # DD Initialize
        if st == 1:
            print("OK")
        else:
            print("Error")
            exit(101)

        # DD虚拟码，可以用DD内置函数转换。
        self.vk = {'5': 205, 'c': 503, 'n': 506, 'z': 501, '3': 203, '1': 201, 'd': 403, '0': 210, 'l': 409, '8': 208,
                   'w': 302,
                   'u': 307, '4': 204, 'e': 303, '[': 311, 'f': 404, 'y': 306, 'x': 502, 'g': 405, 'v': 504, 'r': 304,
                   'i': 308,
                   'a': 401, 'm': 507, 'h': 406, '.': 509, ',': 508, ']': 312, '/': 510, '6': 206, '2': 202, 'b': 505,
                   'k': 408,
                   '7': 207, 'q': 301, "'": 411, '\\': 313, 'j': 407, '`': 200, '9': 209, 'p': 310, 'o': 309, 't': 305,
                   '-': 211,
                   '=': 212, 's': 402, ';': 410}
        # 需要组合shift的按键。
        self.vk2 = {'"': "'", '#': '3', ')': '0', '^': '6', '?': '/', '>': '.', '<': ',', '+': '=', '*': '8', '&': '7',
                    '{': '[', '_': '-',
                    '|': '\\', '~': '`', ':': ';', '$': '4', '}': ']', '%': '5', '@': '2', '!': '1', '(': '9'}

    def down_up(self, code):
        # 进行一组按键。(1：按下；2：抬起)

        self.dd_dll.DD_key(self.vk[code], 1)
        self.dd_dll.DD_key(self.vk[code], 2)

    def down_up1(self):
        # 进行一组按键。(1：按下；2：抬起)

        self.dd_dll.DD_key(601, 1)
        print("进行一组按键。(1：按下；2：抬起)")
        self.dd_dll.DD_key(601, 2)

    def dd(self, i):  # 自己可以定义各种操作
        # 500是shift键码。
        if i.isupper():
            # 如果想输入大写，先按下shift,再输入字母，然后松掉shift。
            # 按下抬起。
            self.dd_dll.DD_key(500, 1)
            self.down_up(i.lower())
            self.dd_dll.DD_key(500, 2)

        elif i in '~!@#$%^&*()_+{}|:"<>?':
            # 输入特殊字符一样的道理。
            self.dd_dll.DD_key(500, 1)
            self.down_up(self.vk2[i])
            self.dd_dll.DD_key(500, 2)
        else:
            # 输入常规的字符
            self.down_up(i.lower())

    # self.dd_dll.DD_key(self.vk[i], 1)
    # time.sleep(1)
    # self.dd_dll.DD_key(self.vk[i], 2)
    def click(self):
        '''模拟鼠标，位置在鼠标位置'''
        self.dd_dll.DD_btn(4)
        self.dd_dll.DD_btn(8)

    def shifang(self):
        win32api.FreeLibrary(self.dd_dll._handle)


if __name__ == "__main__":
    op = op_keyboard()
    # op.down_up1()
    for i in 'ck05140011':
        op.down_up(i)
    op.shifang()
