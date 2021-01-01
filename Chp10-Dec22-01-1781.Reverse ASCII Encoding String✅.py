# https://www.jiuzhang.com/course/84/dialog/#chapter-462_1

# 79_76_76_69_72
# 01_23_45_67_89
# len(string) = 10

str_1 = '7976766972'
str_2 = '656667'

# str_1 = '79767669727976766972'

# 🤏 👑 ✅ Template:


def reverse_func_temp(string):
    result = ""  # Empty container
    k = 2  # K-step: can be ANY integer

    for i in range(len(string) - 1, -1, -k):
        num = int(string[(i - (k-1)):(i + 1)])
        result += chr(num)

    return result


print(reverse_func_temp(str_1))

print(reverse_func_temp(str_2))


def reverse_func(string):
    # Create empty result as the "string container" ("HELLO")
    result = ""

    # Perform the Conversion/Translation
    # 👑 🧠 for i in range(len(string) -1, -1, -k)
    for i in range(len(string) - 1, -1, -2):
        # 1 of 3: locate each slot by 2 step
        # 2 of 3: convert string into number (integer)
        # 3 of 3: store as number variable
        num = int(string[(i - 1):(i + 1)])
        # 1 of 2: search each number with reference from the ASCII Index
        # 2 of 2: store the "translated" text into "string container" (😎 += add with itself)
        result += chr(num)

    return result


print(reverse_func(str_1))

print(reverse_func(str_2))

"""
Take-away Notes:
1. There is this "fixed" relationship between actual length and the index associated with it.
2. We must first convert 🧠 len(string) - 1 to fit into the context of Indexing numbers
3. Then, apply the reverse sequence with 🧠 (start, stop=0, step=-2)
4. Another nice trick is to remember 🧠 [(i - 1):(i + 1)] as [Inclusive : Not-inclusive]
5. Convert into integer and store them as number; finally add them back to the += container
"""


# Challenge - 1: create ⏮ reverse which starts at len(string) - 2

def reverse_func_1(string):
    result = ""

    for i in range(len(string)-2, -1, -2):
        num = int(string[i:(i + 2)])
        result += chr(num)

    return result


print(reverse_func_1(str_1))
print(reverse_func_1(str_2))

# Challenge - 2: create ⏭ forward sequence


def forward_func_2(string):
    result = ""

    # 👑 🧠 for i in range(0, len(string), k)
    for i in range(0, len(string), 2):
        num = int(string[i:(i + 2)])
        result += chr(num)

    result = result[-1:-len(result)-1:-1]

    return result


print(forward_func_2(str_1))
print(forward_func_2(str_2))

# Challenge - 3: convert all strings with corresponding lower case numbers


def reverse_func_3(string):
    result = ""
    convert_margin = 32
    num_step = -2

    for i in range(len(string)-1, -1, num_step):
        num = int(string[(i - 1): (i + 1)]) + convert_margin
        result += chr(num)

    return result


print(reverse_func_3(str_1))
print(reverse_func_3(str_2))


def reverseString_4(string):
    if string is None:
        return ""

    answer = ""

    for i in range(0, len(string), 2):
        num = int(string[i:i+2])
        answer += chr(num)  # Can we use answer.append()?
    return answer[::-1]


str_1 = '7976766972'
str_2 = '656667'

print(reverseString_4(str_1))
print(reverseString_4(str_2))
