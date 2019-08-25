# def foo(n):
#     ans = 0
#     while n >0:
#         yu = n % 6
#         ans  = ans*6 +  yu
#         n = n //6
#     print(ans)
#
# n= 1000000
# foo(n)

def foo():
    sum = 0
    for i in range(1,11):
        sum += i
    print(sum/(26*26))
# foo()

def foo():

    sum = 0
    for i in range(1,53):
        sum += 1/i
    print(sum)
# foo()
import math
def foo(n):
    if n<2:
        return 1
    return foo(n//2) + foo(n//4)
# 求foo(12345678987654321)
print(foo(17))
print(math.log(17,2),math.log(17,4))

print(foo(84))
print(math.log(84,2),math.log(84,4))
