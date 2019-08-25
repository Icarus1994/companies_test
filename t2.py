#coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。
import sys
if __name__ == "__main__":
    # 读取第一行的n
    line1 = sys.stdin.readline().strip()
    n,m = list(map(int, line1.split()))[0], list(map(int, line1.split()))[1]
    # 1000000创建数组时间过长
    matrix = [[0 for i in range(m)] for i in range(n)]
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        matrix[i] = list(map(int, line.split()))
    print(matrix)
