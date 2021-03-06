#   6. Реализовать два небольших скрипта:
#   итератор, генерирующий целые числа, начиная с указанного;
#   итератор, повторяющий элементы некоторого списка, определённого заранее.
#   Подсказка: используйте функцию count() и cycle() модуля itertools.
#   Обратите внимание, что создаваемый цикл не должен быть бесконечным.
#   Предусмотрите условие его завершения. #### Например, в первом задании выводим целые числа, начиная с 3.
#   При достижении числа 10 — завершаем цикл. Вторым пунктом необходимо предусмотреть условие, при котором повторение элементов списка прекратится.


from sys import argv
from itertools import cycle
from random import randint


arg_1, arg_2 = map(int, argv[1:])   #   Вводим два числа: 1-е Количество элементов в списке
                                    #   2-e число количество выведенных элементов
                                    #   Пример: python gb_hw_004_06_2.py 20 50

b = 1
my_list = (randint(1, 100) for i in range(arg_1))
print(my_list)
for i in cycle(my_list):
    if b > arg_2:
        break
    else:
        b += 1
        print(i, end=' ')