# Python slicing

# 🧠 明确定义的矢量遵循规定方向，不然为空[ ]!

# 🎯 how to convert a, b, c with quotes auaomaticallly!

#          0    1    2    3    4    5    6
#          -7   -6   -5   -4   -3   -2   -1
list_s = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# print(len(list_s))

# print(list_s[1:4:1])
# print(list_s[0:6:2])
# print(list_s[0::2])
# print(list_s[2:-2:2])
# print(list_s[-6:-2:1])
# print(list_s[0:8:2])

print(list_s[::1])  # ⏭
print(list_s[::-1])  # ⏮
print()

print(list_s[::2])
print(list_s[::-2])
print()


print(list_s[-3:5:1])
print(list_s[-3:5:-1])
print()

print(list_s[4:5:1])
print(list_s[4:5:-1])
print()

print(list_s[-6:5:1])
print(list_s[-6:5:-1])
print()

print(list_s[1:-2:1])
print(list_s[1:-2:-1])
print()

print(list_s[1:-2:2])
print(list_s[1:-2:-2])
print()

print(list_s[0:-7:-1])
print()

print(list_s[-4:-2:-2])
print(list_s[-4:-2:2])
print()

print(list_s[-4::-2])
print(list_s[-4::2])
print()

print(list_s[4::-2])
print(list_s[4::2])
print()

print(list_s[0:-7:1])
print(list_s[0:-7:-1])
print()

print(list_s[-9:9:1])
print(list_s[-9:9:-1])
print()
