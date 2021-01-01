"""
string = a, a, a, a, a, b, b, c, c, d, d

for i in set(string):
    count frequency of i in string
    if there is more than 1 frequency % 2 == 1:
        return NO
    else:
        return Yes


"""


def getStream(string):
    # 出现次数为奇数的字母 <= 1
    if string is None:
        return ''

    answer = []
    count = 0
    alphabet = [0] * 26
    # 0 -> a, 1-> b, ... 25 -> z

    for i in range(len(string)):
        alphabet[ord(string[i]) - ord('a')] += 1

        # NOTE: 锁定每一个对应的字母
        if alphabet[ord(string[i]) - ord('a')] % 2 == 1:
            count += 1
        else:
            count -= 1

        if count > 1:
            answer.append(0)
        else:
            answer.append(1)

    return answer


str_1 = ['a', 'a', 'a', 'a', 'a']
str_2 = ['a', 'b', 'c', 'b', 'a']
str_3 = ['a', 'a', 'z', 'z', 'b']

print(getStream(str_1))
print(getStream(str_2))
print(getStream(str_3))
