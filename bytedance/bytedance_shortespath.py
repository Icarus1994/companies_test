class Solution:
    # n行m列
    def findPath(self, matrix, n, m):
        if n > 1000 or m > 1000 or n < 2 or m < 2:
            print(0)
            return None

        # aggre[i][j]存放（0，0）到（i,j）位置后缀0最少的乘积（十进制数）
        aggre = [[1] * m for i in range(n)]
        path = [[''] * m for i in range(n)]
        aggre[0][0] = int(str(matrix[0][0]),16)
        for j in range(1,m):
            path[0][j] += '0'
            aggre[0][j] *= aggre[0][j-1]
        for i in range(1,n):
            path[i][0] += '1'
            aggre[i][0] *= aggre[i-1][0]

        for i in range(1,n):
            for j in range(1,m):
                from_left = aggre[i][j-1] * int(str(matrix[i][j]),16)
                from_top = aggre[i-1][j] * int(str(matrix[i][j]),16)
                if self.count0Num(from_left) > self.count0Num(from_top):
                    path[i][j] += '1'
                    aggre[i][j] = from_top
                elif self.count0Num(from_left) < self.count0Num(from_top):
                    path[i][j] += '0'
                    aggre[i][j] = from_left
                else:
                    aggre[i][j] = from_left
                    if path[i][j-1] < path[i-1][j]:
                        path[i][j] = path[i][j-1] + '0'
                    else:
                        path[i][j] = path[i-1][j] + '1'
        # python两行的print会自动换行
        print(self.count0Num(aggre[n-1][m-1]))

        res = ''
        for c in path[n-1][m-1]:
            res += '>' if c == '0' else 'V'
        print(res)

    def count0Num(self,num):
        cnt = 0
        while num>0:
            if num %16 == 0:
                cnt +=1
                num /= 16
            else:
                break
        return cnt

if __name__ == '__main__':
    matrix = [[3,2,8],['c',8,8],[2,'a','f']]
    n,m = 3,3
    Solution().findPath(matrix,n,m)


