# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)
print('Введите трехзначное число:')
N = int(input())
sum = 0
while N > 0:
    sum += N % 10
    N = N // 10
print(sum)