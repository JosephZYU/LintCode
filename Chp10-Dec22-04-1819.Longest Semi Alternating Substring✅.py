# b_aaa_bb_a_bbb
# 0_123_45_6_789

def longestSemiAltSubstring(string):
    # Edge case
    if string is None or len(string) < 3:
        return len(string)

    # Regular case
    left = 0
    # right = [1, 2, 3, ..., len(string)]
    consec_count = 1  # condition -> +=1
    max_len = 0  # condition -> max(max_len, right - left + 1)

    for right in range(1, len(string), 1):
        if string[right] == string[right - 1]:
            consec_count += 1
            if consec_count == 3:
                left = right - 1
                consec_count = 2
        else:
            consec_count = 1

        max_len = max(max_len, right - left + 1)

    return max_len


str_1 = 'baaabbabbb'
str_2 = 'ba'
str_3 = 'a'
str_4 = ''
str_5 = 'aaa'

print(longestSemiAltSubstring(str_1))
print(longestSemiAltSubstring(str_2))
print(longestSemiAltSubstring(str_3))
print(longestSemiAltSubstring(str_4))
print(longestSemiAltSubstring(str_5))
