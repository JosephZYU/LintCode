"""
Input: s = ['a', 'a', 'a', 'a', 'a']
Output: [1, 1, 1, 1, 1]

chr(97, 87, 99)
ord(a, b, c)

1. 出现次数(frequency)为奇数的字母的个数小于等于1
2. create the complete alphabetical list for base of freqneyc count
3. odd number count

"""


def isStream(string):

    if not string:
        return []

    result = []
    baseNum = ord('a')
    count = 0
    alphabet = [0] * 26

    for i in string:
        index = ord(i) - baseNum
        alphabet[index] += 1

        if alphabet[index] % 2 == 1:
            count += 1
        else:
            count -= 1

        if count <= 1:
            result.append(1)  # NOTE: result.append(int) DIRECTLY!
        else:
            result.append(0)

    return result


str_1 = ['a', 'b', 'a']
str_2 = ['a', 'b', 'b', 'c']
str_3 = []
str_4 = ['a', 'b', 'b']
str_5 = ['a', 'a', 'a', 'a', 'b']

print(isStream(str_1))
print(isStream(str_2))
print(isStream(str_3))
print(isStream(str_4))
print(isStream(str_5))
