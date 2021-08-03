import matplotlib.pyplot as plt
import math
import numpy as np


def method_rectangles(x3, x2, x1, k, a, b, eps, n):
    answer = mid(x3, x2, x1, k, a, b, eps, n)
    answer += left(x3, x2, x1, k, a, b, eps, n)
    answer += right(x3, x2, x1, k, a, b, eps, n)
    return answer

def mid(x3, x2, x1, k, a, b, eps, n):
    mid = rectangle_mid(x3, x2, x1, k, a, b, n)
    n *= 2
    mid1 = rectangle_mid(x3, x2, x1, k, a, b, n)
    while (abs(mid1 - mid) > eps ):
        mid = mid1
        n *= 2
        mid1 = rectangle_mid(x3, x2, x1, k, a, b, n)

    finalSteps = int(n/2)
    answer = 'По методу центральных прямоугольников ответ: ' + str(
        rectangle_mid(x3, x2, x1, k, a, b, n)) + '. Количество разбиений ' + str(finalSteps) + '.\n'
    return answer

def left(x3, x2, x1, k, a, b, eps, n):
    left = rectangle_left(x3, x2, x1, k, a, b, n)
    n *= 2
    left1 = rectangle_left(x3, x2, x1, k, a, b, n)
    while (abs(left1 - left) > eps):
        left = left1
        n *= 2
        left1 = rectangle_left(x3, x2, x1, k, a, b, n)

    finalSteps = int(n / 2)
    answer = 'По методу левых прямоугольников ' + str(
        rectangle_left(x3, x2, x1, k, a, b, n)) + '. Количество разбиений ' + str(
        finalSteps) + '.\n'
    return answer

def right(x3, x2, x1, k, a, b, eps, n):
    right = rectangle_right(x3, x2, x1, k, a, b, n)
    n *= 2
    right1 = rectangle_right(x3, x2, x1, k, a, b, n)
    while (abs(right1 - right) > eps):
        right = right1
        n *= 2
        right1 = rectangle_right(x3, x2, x1, k, a, b, n)
    finalSteps = int(n / 2)
    answer = 'По методу правых прямоугольников ' + str(
        rectangle_right(x3, x2, x1, k, a, b, n)) + '. Количество разбиений ' + str(
        finalSteps) + '.\n'
    return answer

def rectangle_mid(x3, x2, x1, k, a, b, n):
    step = (b - a) / n
    sum = 0
    for i in range(0, n):
        sum += f(a + step / 2, x3, x2, x1, k)
        a += step
    sum *= step
    return sum


def rectangle_left(x3, x2, x1, k, a, b, n):
    step = (b - a) / n
    sum = 0
    for i in range(0, n):
        sum += f(a, x3, x2, x1, k)
        a += step
    sum *= step
    return sum


def rectangle_right(x3, x2, x1, k, a, b, n):
    step = (b - a) / n
    a += step
    sum = 0
    for i in range(0, n):
        sum += f(a, x3, x2, x1, k)
        a += step
    sum *= step
    return sum


def method_trapezium(x3, x2, x1, k, a, b, eps, n):
    sum = sumOfTrapeziums(x3, x2, x1, k, a, b, n)
    n *= 2
    n_sum = sumOfTrapeziums(x3, x2, x1, k, a, b, n)
    while (abs(n_sum - sum) > eps):
        sum = n_sum
        n *= 2
        n_sum = sumOfTrapeziums(x3, x2, x1, k, a, b, n)

    finalSteps = int(n/2)
    return 'По методу трапеций ответ: ' + str(sum) + '. Количество разбиений ' + str(finalSteps) + '.'


def sumOfTrapeziums(x3, x2, x1, k, a, b, n):
    step = (b - a) / n
    sum = 0
    for i in range(0, n):
        y0 = f(a, x3, x2, x1, k)
        a += step
        yn = f(a, x3, x2, x1, k)
        sum += step * (y0 + yn) / 2
    return sum


def Simpsons_method(x3, x2, x1, k, a, b, eps, n):
    sum = Simpsons_formula(x3, x2, x1, k, a, b, n)
    n *= 2
    n_sum = Simpsons_formula(x3, x2, x1, k, a, b, n)
    while (abs(n_sum - sum) > eps):
        sum = n_sum
        n *= 2
        n_sum = Simpsons_formula(x3, x2, x1, k, a, b, n)
    finalSteps = int(n/2)
    return 'Ответ: ' + str(sum) + '. Количество разбиений ' + str(finalSteps) + '.'

def Simpsons_formula(x3, x2, x1, k, a, b, n):
    step = (b - a) / n
    x0 = f(a, x3, x2, x1, k)
    a += step
    xn = f(b, x3, x2, x1, k)
    sum_1 = 0
    sum_2 = 0
    for i in range(1, n):
        if (i % 2 == 0):
            sum_2 += f(a, x3, x2, x1, k)
        else:
            sum_1 += f(a, x3, x2, x1, k)
        a += step
    answer = step * (x0 + xn + 2 * sum_2 + 4 * sum_1) / 3
    return answer


def f(x, x3, x2, x1, k):
    return x3 * pow(x, 3) + x2 * pow(x, 2) + x1 * x + k


if __name__ == '__main__':
    answerGiven = True
    scannerline = True

    while scannerline:
        print('Ввод из файла/из строки (1/0): ')
        mes = input()
        if mes == '1':
            try:
                path = open('lol', 'r')
                x3, x2, x1, k = map(float, path.readline().split(' '))
                a, b = map(float, path.readline().split(' '))
                eps = float(path.readline())
                n = int(path.readline())


                answerGiven = True
                scannerline = False
            finally:
                path.close()
        else:
            print('Коэффициент перед x^3: ')
            x3 = float(input())
            print('Коэффициент перед x^2: ')
            x2 = float(input())
            print('Коэффициент перед x^1: ')
            x1 = float(input())
            print('Свободный член: ')
            k = float(input())
            print('Нижний предел интегрирования: ')
            a = float(input())
            print('Верхний предел интегрирования: ')
            b = float(input())
            print('Погрешность: ')
            eps = float(input())
            print('Начальное значение числа разбиения интервала интегрирования: ')
            n = int(input())

            answerGiven = True
            scannerline = False

    print('Выберите метод: \n' +
          '1. Метод прямоугольников (3 модификации: левые, правые, средние) \n' +
          '2. Метод трапеций \n' +
          '3. Метод Симпсона \n' +
          '4. Прямое вычисление \n' +
          'Ваш ответ: ')
    answer = ''

    while answerGiven:
        give = input()
        if give == '1':
            answer = method_rectangles(x3, x2, x1, k, a, b, eps, n)
            answerGiven = False
        elif give == '2':
            answer = method_trapezium(x3, x2, x1, k, a, b, eps, n)
            answerGiven = False
        elif give == '3':
            answer = Simpsons_method(x3, x2, x1, k, a, b, eps, n)
            answerGiven = False
        elif give == '4':
            answer = Nioton(x3, x2, x1, k, a, b, eps)
            answerGiven = False
        else:
            print('Ошибка: не тот номер \n' +
                  'попробуйте еще раз')
            continue

    print('Вывести в файл/консоль(1/0)')
    viv = input()
    if viv == '1':
        try:
            with open('l.txt', 'w') as file:
                file.writelines(answer)
        except:
            print("Ошибка: решений нет")
        finally:
            file.close()
    else:
        if (answer != 0):
            print(answer)
        else:
            print("Ошибка: решений нет")
