def numberOfOperations(string):
    # 'abba'
    # ||
    if string is None:
        return 0

    min_step = 0
    left, right = 0, len(string) - 1

    # while left >= right: return
    while left < right:
        min_step += abs(ord(string[left]) - ord(string[right]))
        left += 1
        right -= 1
    return min_step


str_1 = 'abc'
str_2 = 'abcd'
str_3 = 'abcdef'

print(numberOfOperations(str_1))
print(numberOfOperations(str_2))
print(numberOfOperations(str_3))
