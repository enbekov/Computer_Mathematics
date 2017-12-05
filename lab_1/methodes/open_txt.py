from math import *

p = r'/home/tanali/PycharmProjects/Computer_Mathematics/lab_1/input'
equations_list = open(p).readlines()


def get_all_equations():  # Получаем все уравнения из файла в список
    for i in range(0, len(equations_list)):
        equations_list[i] = equations_list[i].rstrip()
    return equations_list


def f(line_number, param):
    array = get_all_equations()
    x = param  # Заменяем все x в уравнении из array переменной param. Заменится после eval(a)
    a = array[int(line_number)]
    b = eval(a)  # Использовать eval() не рекомендуется по соображениям безопастности
    return b     # Я ищу другие способы. Нужно использовать математические библиотеки типа numpy

