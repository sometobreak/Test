import random
# Рекурсивный алгоритм сортировки с указанием диапазона ндексов массива
def sort(nums_list, first_index, last_index):
    # завершаем рекурсию
    if first_index >= last_index: return
    # инициализация указателей и случайного разделителя
    i, j = first_index, last_index
    divider = nums_list[random.randint(first_index, last_index)]
    # сдвигаем указатель i вправо и указатель j влево к разделителю
    while i <= j:
        # получаем элемент с индексом i, который больше
        # или равен разделителя
        while nums_list[i] < divider: i += 1
        # получаем элемент с индексом j, который меньше
        # или равен разделителя
        while nums_list[j] > divider: j -= 1
        # если указатели не разошлись, меняем элементы массива местами
        if i <= j:
            nums_list[i], nums_list[j] = nums_list[j], nums_list[i]
            i, j = i + 1, j - 1
    # вызываем функцию заного        
    sort(nums_list, first_index, j)
    sort(nums_list, i, last_index)


numbers = [8, 1, 7, 3, 6, 0, 9, 5, 4, 2]
sort(numbers, 0, len(numbers) -1)
print(numbers)

# Простой и быстрый алгоритм, за исключением случаев,
# когда массив уже отсортирован или разделитель всегда
# находится с краю. Также + этого метода в том, что он
# работает с самим массивом, не требуя дополнительной памяти
