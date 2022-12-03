#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
"""""
Объявите функцию с именем get_sq , которая вычисляет площадь прямоугольника по двум
параметрам: width и height – ширина и высота прямоугольника и возвращает результат.
Определите декоратор для этой функции с именем (внешней функции) func_show , который
отображает результат на экране в виде строки (без кавычек): "Площадь прямоугольника:
<значение>". Вызовите декорированную функцию get_sq .
"""""


def func_show(func):
    def wrapper(*args):
        rw = 1
        for i in args:
            rw *= i
            res = func(*args)
        print(f"Площадь прямоугольника: {res}")
        return res

    return wrapper


@func_show
def get_sq(*args):
    r = 1
    for num in args:
        r *= num
    return r


if __name__ == '__main__':
    w = int(input("Введите ширину: "))
    h = int(input("Введите высоту: "))
    get_sq(w, h)
