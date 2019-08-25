class Solution:
    def trap(self, height):
        if not height or len(height) == 1 or len(height) == 2:
            return 0
        max = p = 0
        for i in range(len(height)):
            if height[i] > max:
                max = height[i]
                p = i
        sum = 0
        max_left = height[0]
        # 边界
        if 1 < p:
            for j in range(1, p):
                if max_left > height[i]:
                    sum += max_left - height[i]
                elif max_left < height[i]:
                    max_left = height[i]
        max_right = height[len(height) - 1]
        if p < len(height) - 2:
            for k in range(len(height) - 2, p, -1):
                if max_right > height[k]:
                    sum += max_right - height[k]
                elif max_right < height[k]:
                    max_right = height[k]
        return sum

    def findLength(self, A, B) -> int:
        if not A or not B:
            return 0
        max = 0
        a = [0] * (len(B) + 1)
        c = [a for i in range(len(A) + 1)]
        for i in range(1, len(A) + 1):
            for j in range(1, len(B) + 1):
                print(i,j)
                if A[i - 1] == B[j - 1]:
                    c[i][j] = c[i - 1][j - 1] + 1
                    # print(c[i][j])
                    if c[i][j] > max:
                        max = c[i][j]
                else:
                    c[i][j] = 0
        print(c)
        return max


if __name__ == '__main__':
    A = [1,2,3,2,1]
    B = [3,2,1,4,7]
    res = Solution().findLength(A,B)
    print(res)

