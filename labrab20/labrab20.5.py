s = input()
s0 = input()
streak = 0
col = 0
for i in range(len(s)):
    if streak == len(s0):
        streak = 0
        col = col + 1
    if s0[streak] == s[i]:
        streak = streak + 1
if streak == len(s0):
    col = col + 1
print(col)
