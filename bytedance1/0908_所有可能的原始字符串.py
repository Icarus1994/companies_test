# -*- coding: utf-8 -*-
# @Time : 2019-09-08 20:03
# @Author : icarusyu
# @FileName: 0908_所有可能的原始字符串.py
# @Software: PyCharm
class solution:
    def __init__(self):
        self.mapping = {}
    def f(self):
        st = input()
        for i in range(1,27):
            self.mapping[str(i)] = chr(i+64)
        self.digui(st,'')

    def digui(self,st,res):
        if st =='':
            print(res)
        else:
            res0 = res + self.mapping[st[0]]
            self.digui(st[1:], res0)
            if len(st) >1 and (st[0] == '1' or (st[0] == '2' and int(st[1]) <= 6)):
                res1 = res + self.mapping[st[:2]]
                self.digui(st[2:],res1)

solution().f()

# 问题
# 将对a-z每个字母映射为数字，A:1,Z:26,依次类推
# 现在有一串字符串格式的数字，要求打印这串数字可能对应的原始字符串的情况，对所有可能的情况按字典顺序打印
# 样例
#input 12
#output
# AB
# L
