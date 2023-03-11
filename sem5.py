#Задача 1
s = input('Введите арифметическое выражение: ')
sum = 0
# min = '-'
# for i in range(0, len(s)-1):
#     if s[i] == min:
#         int(s[i+1]) = int(s[i+1]*(-1))
for i in range(0, len(s), 2):
        sum = sum + int(s[i])
print(sum)
