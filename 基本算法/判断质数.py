# -*- coding: utf-8 -*-
# @Time : 2019-11-03 21:37
# @Author : icarusyu
# @FileName: 判断质数.py
# @Software: PyCharm
'''
# 问题：求给定区间[a,b]内素数个数
建立长度为b的素数表lst，开始全为true
从i=2开始,将lst中下标为2倍数的元素置false
i=3,若i为素数（b[i]==true）,则将素数的倍数都置为false
对区间内的lst求和
参考：https://www.cnblogs.com/cmmdc/p/7202704.html

'''