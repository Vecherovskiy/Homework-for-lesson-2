import numpy as np


# Написать функцию, которая для заданной квадратной матрицы считает сумму её диагональных элементов.
def task_1(matrix):
    if len(matrix) == 1:  # для матриц вида [[5]]
        return np.trace(np.asarray(matrix))
    if len(matrix) % 2:  # ищем центральный элемент в матрице
        i = len(matrix) % 2
        center_elem = matrix[i][i]
    else:
        center_elem = 0
    m = np.asarray(matrix)
    diag_sum = np.trace(m)  # сумма диагонали
    m = np.fliplr(m)  # перевернули матрицу
    antidiag_sum = np.trace(m)  # сумма антидиагонали
    return diag_sum + antidiag_sum - abs(center_elem)  # сложили сумму диагонали и антидиагонали, вычли центральный эл-т


# Перемешать строку по шаблону. Написать функцию, которая перемешивает буквы строки согласно предоставленному порядку.
def task_2(s, indices):
    result = ''  # строка, в которой складываем результат
    for i in indices:  # для каждого индекса в списке индексов...
        result += s[i]  # взять i-ый элемент из начальной строки s и добавить его в результирующую строку
    return result


def task_3(line_4th):
    temp_data = (line_4th.split(' '))[3]  # разбить 4-ю строку на блоки, данные о температуре содержатся в 3-м блоке
    is_above_zero = temp_data[1] == '0'  # температура выше 0С, если 1-й символ в 3-м блоке - это "0"
    degrees = int(temp_data[-3:])  # переводим градусы в число, минимальная единица - одна десятая градуса С
    if is_above_zero:
        return f'{degrees // 10},{degrees % 10} °'  # тогда целое значение градусов - значение degrees деленное без
        # остатка на 10, а дробное значение - остаток от деления на 10
    return f'-{degrees // 10},{degrees % 10} °'
