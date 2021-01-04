# 相向双指针
# 直到“左指针”大于等于右指针时：return

# https://stackoverflow.com/a/227472

# [97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122]
# a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z,


str_1 = 'abcd'
str_2 = ''
str_3 = 'aa'
str_4 = 'ab'
str_5 = 'aba'


def minSteps(string):

    left, right = 0, len(string) - 1
    steps = 0

    if not string:
        return 0

    while left < right:
        steps += abs(ord(string[left]) - ord(string[right]))
        left += 1
        right -= 1

    return steps


print(minSteps(str_1))
print(minSteps(str_2))
print(minSteps(str_3))
print(minSteps(str_4))
print(minSteps(str_5))
