# #Задача 1
# s = input('Введите арифметическое выражение: ')
# sum = 0
# # min = '-'
# # for i in range(0, len(s)-1):
# #     if s[i] == min:
# #         int(s[i+1]) = int(s[i+1]*(-1))
# for i in range(0, len(s), 2):
#         sum = sum + int(s[i])
# print(sum)

#Задача 26
def power(a, b):
    if (b == 1):
        return (a)
    if (b != 1):
        return (a * power(a, b - 1))
a = int(input("Введите число: "))
b = int(input("Введите его степень: "))
print("Результат возведения в степень равен:", power(a, b))