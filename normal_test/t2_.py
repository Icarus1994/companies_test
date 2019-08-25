import sys
def f():
    ans = False
    str1 = sys.stdin.readline().strip()
    arr = ['']*10000
    line = sys.stdin.readline().strip()
    arr = list(map(str, line.split()))
    length = len(list(map(str, line.split())))
    while length>0:
        if arr[length-1][0] == str1[0]:
            for j in range(len(arr[0])):
                if arr[j] == str1[j]:
                    pass
                else:
                    break
            if j == len(arr[0])-1:
                length -=1
                str1 = str1[j+1:]

    if str1 == '':
        ans = True
    print(ans)
