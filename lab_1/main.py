from methodes.bisection import calc_bisect  # Метод бисекции или дихотомии
from methodes.chordes import calc_chord  # Метод ход
from methodes.newton import calc_newton  # Метод Ньютона или касательных
from methodes.open_txt import equations_list  # Импортируем список из уравнений которые нам нужно решить


def main():
    print('--------------------')
    print('bisect')
    for i in range(len(equations_list)):
        print(equations_list[i], "; answer: ", calc_bisect(i))
    print('--------------------')
    print('chord')
    for i in range(len(equations_list)):
        print(equations_list[i], "; answer: ", calc_chord(i))
    print('--------------------')
    print('newton')
    a = float(input('Введите начальное приближение: '))
    for i in range(len(equations_list)):
        print(equations_list[i], "; answer: ", calc_newton(i, a))


if __name__ == '__main__':
    main()


