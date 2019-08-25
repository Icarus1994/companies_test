#coding=utf-8
# 本题为考试单行多行输入输出规范示例，无需提交，不计分。
import sys


def repeatStr(str):
    res = ''
    if '%' not in str:
        return str
    i,j = 0,0
    while i< len(str):
        if str[i].isdigit():
            cnt = int(str[i])
        # 处理在'%'之前和'#'之后的字符，这些字符只需要原样打印
        elif str[i].isalpha():
            res+=str[i]
        elif str[i] == '%':
            m = 1
            for j in range(i+1,len(str)):
                if str[j] == '#':
                    m-=1
                elif str[j] == '%':
                    m+=1
                if m == 0:
                    break
            res += cnt * repeatStr(str[i+1:j])
        i = max(i+1,j)
    return res

if __name__ == '__main__':
    str = sys.stdin.readline().strip()
    print(repeatStr(str))

# 题目
# 给出一个字符串，要求字符串重复%之前数字的倍数输出（数字小于10），字符串以#结尾。可能有嵌套%#的情况
# eg.3%g2%n##,输出gnngnngnn

# 思路
# 递归地输出字符串，边界条件为当字符串中不含%#时。当有嵌套重复字符串时递归调用函数自身

# 细节
# 含嵌套字符串时，在内层重复字符串之外，外层重复字符串之间的字符也要原样输出
# 题目没给定时要考虑重复次数大于10的情况




