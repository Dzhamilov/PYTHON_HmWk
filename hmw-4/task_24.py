# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. 
# Она растет на круглой грядке, причем кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет
# N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них 
# выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может 
# собрать за один заход собирающий модуль, находясь перед некоторым кустом 
# заданной во входном списке содержащим количество ягод на кустах.
bush = list(map(int, input().split()))
max_berr = 0
if len(bush) >= 3:
    for i in range(len(bush)):
        bush_3 = bush[i - 2] + bush[i - 1] + bush[i]
        if bush_3 > max_berr:
            max_berr = bush_3
    print(max_berr)
else:
    print('ERROR')