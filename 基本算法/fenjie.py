def reduceNum(n):
    print ('{} = '.format(n),)
    if not isinstance(n, int) or n <= 0 :
        exit(0)
    elif n in [1] :
        print('{}'.format(n))
    while n != 1: # 循环保证递归
        # 可以从2-Nl连续遍历来除N是因为当遇到合数时不会有N/合数==0，因为N会被能分解合数的数先整除
        for index in range(2,n + 1) :
            if n % index == 0:
                n /= index # n 等于 n/index
                if n == 1:
                    print(index)
                else : # index 一定是素数
                    print ('{} *'.format(index),)
                break
print(reduceNum(90))