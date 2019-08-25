# -*- coding: utf-8 -*-
# @Time : 2019-08-11 11:16
# @Author : icarusyu
# @FileName: 0811pdd.py.py
# @Software: PyCharm
import sys
class test:
    def test_input(self):
        # for line in sys.stdin:
        #     arr = line.split()
        #     print(type(line),arr)
        line = sys.stdin.readline().strip()
        print(type(line),'\n',line)
        print(type(sys.stdin))
test().test_input()