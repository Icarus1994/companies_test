#coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。
import sys
if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    # values读取第二行数组
    values = list(map(int, line.split()))
    max_score = -1000
    if n == 1:
        print(values[0])
    elif n <=0:
        print(0)
    else:
        for i in range(n-1):
            for j in range(i+1,n):
                score = values[i] + values[j] - (j - i)
                # max_score = max(max_score,score)
                if score > max_score:
                    max_score = score
        print(max_score)


