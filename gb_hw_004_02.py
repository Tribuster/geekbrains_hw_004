#   2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых
#   больше предыдущего элемента.
#   Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
#   Для его формирования используйте генератор.
#   Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
#   Результат: [12, 44, 4, 10, 78, 123].

from random import randint

my_list = [randint(1, 1000) for i in range(20)]
print(my_list)

#new_list = [el for el in my_list[1:] if my_list[el] > my_list[el - 1]]
new_list = []
for i in range(1, len(my_list)):
    if my_list[i] > my_list[i-1]:
        (new_list.append(my_list[i]))
print(new_list)