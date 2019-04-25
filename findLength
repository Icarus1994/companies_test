class Solution:
    def findLength(self, A, B):
        if not A or not B or len(A) == 0 or len(B) == 0:
            return 0
        up = [0 for i in range(len(A) + 1)]
        down = [0 for i in range(len(A) + 1)]
        # B作为二维数组的列
        for i in range(1, len(B) + 1):
            for j in range(1, len(A) + 1):
                if B[i - 1] == A[j - 1]:
                    down[j] = up[j - 1] + 1
                else:
                    down[j] = max(down[j - 1], up[j])
            up = down
            down = [0 for i in range(len(A) + 1)]
        return up[-1]


A = [1, 2, 3, 2, 1]
B = [3, 2, 1, 4, 7]
ans = Solution().findLength(A, B)
print(ans)

# 原理参考
# https://blog.csdn.net/hrn1216/article/details/51534607

