"""
Input: "7976766972"
Output: "HELLO"

01-23-45-67-89
79-76-76-69-72


class Solution:
    # @param encoding: an encoding string
    # @return: a reversed decoded string
    
    def reverseAsciiEncodedString(self, encodeString):

        result = ""  # 🧠 output has to be string NOT []

        for i in range(0, len(encodeString), 2):
            num = int(encodeString[i:i+2])
            alpha = chr(num)  # 🧠 chr: 3 letters ONLY!
            result += alpha

        return result[::-1]
"""


def reverseString(encodeString):

    if not encodeString:
        return ""

    result = ""  # NOTE: your output has to be a string
    k = 2

    # ✅ test k-step: 3 - YES
    for i in range(0, len(encodeString), k):
        # ✅ Do we have to convert? - YES. have to convert first!
        num = int(encodeString[i:i+k])
        alpha = chr(num)
        result += alpha
        # ✅ figure append: list-only 🆚 +=: for string
        # NOTE: Strings are immutable -- you can't append to them.

    return result[::-1]


list_a = '7976766972'

list_b = ''

list_c = '656667'


print(reverseString(list_a))
print(reverseString(list_b))
print(reverseString(list_c))
