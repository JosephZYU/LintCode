# [0, 1, 1, 2, 3, 5, 8, 13, ...]
#  1, 2, 3, 4, 5, 6, 7, 8
"""
# 基本解法
def fibonacci(n):
    if n < 1:
        return -1
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(7))
print(fibonacci(8))
print(fibonacci(9))
"""
# 升级解法 - 在递归的同时进行最优化搜索


def get_fibonacci(n, arr):
    if n == 1 or n == 2 or arr[n] > 0:
        return arr[n]

    arr[n] = get_fibonacci(n - 1, arr) + get_fibonacci(n - 2, arr)

    return arr[n]


def fibonacci(n):
    if n < 1:
        return -1
    elif n == 1:
        return 0

    # 记忆化搜索🔍，防止重复计算
    # 使用👇一个array，用来记录之前算过的值，存入array中
    # [0, 0, 1, 0, 0, 0, 0, 0, ...]
    # NOTE: [0 for _ in range(26)] == [0] * 26
    arr = [0 for _ in range(n + 1)]
    arr[2] = 1

    # 递归求解
    return get_fibonacci(n, arr)
