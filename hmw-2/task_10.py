# Задача 10: На столе лежат n монеток. 
# Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

n = int(input('Введите количество монеток: '))
coat = 0  # количество монет стороной гербом (1)
tail = 0  # количество монет стороной решкой (0)
import random
for i in range(n):
    a = random.randint(0,1)
    print(a)
    if a == 1: coat += 1
    else: tail += 1
min = coat
if tail < coat: min = tail
print(f"Минимальное количество монет, которые нужно перевернуть -> {min}")